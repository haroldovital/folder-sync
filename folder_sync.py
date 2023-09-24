import os
import shutil
import sys
import time
import logging

# Set up logging to both console and a log file
log_file = sys.argv[4]
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def sync_folders(source_path, replica_path):
    try:
        # Ensure the source folder exists
        if not os.path.exists(source_path):
            logging.error(f"Source folder '{source_path}' does not exist.")
            return
        # Ensure the replica folder exists or create it
        if not os.path.exists(replica_path):
            os.makedirs(replica_path)
            logging.info(f"Replica folder '{replica_path}' created.")
        
        for root, _, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                rel_path = os.path.relpath(src_file, source_path)
                dest_file = os.path.join(replica_path, rel_path)

                # Check if the file exists in the replica folder
                if not os.path.exists(dest_file):
                    shutil.copy2(src_file, dest_file)
                    logging.info(f"File copied: '{src_file}' to '{dest_file}'")
                else:
                    src_mtime = os.path.getmtime(src_file)
                    dest_mtime = os.path.getmtime(dest_file)

                    # If the source file is newer, copy it to the replica folder
                    if src_mtime > dest_mtime:
                        shutil.copy2(src_file, dest_file)
                        logging.info(f"File copied (updated): '{src_file}' to '{dest_file}'")
        
        # Remove files from the replica folder if they don't exist in the source folder
        for root, _, files in os.walk(replica_path):
            for file in files:
                dest_file = os.path.join(root, file)
                rel_path = os.path.relpath(dest_file, replica_path)
                src_file = os.path.join(source_path, rel_path)

                if not os.path.exists(src_file):
                    os.remove(dest_file)
                    logging.info(f"File removed: '{dest_file}'")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python sync_folders.py <source_path> <replica_path> <sync_interval_seconds> <log_file>")
        sys.exit(1)

    source_path = sys.argv[1]
    replica_path = sys.argv[2]
    sync_interval = int(sys.argv[3])

    while True:
        sync_folders(source_path, replica_path)
        logging.info("Synchronization completed.")
        time.sleep(sync_interval)
