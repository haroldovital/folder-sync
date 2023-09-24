# folder-sync - Folder Synchronization Script

This Python script allows you to synchronize two folders, maintaining a full, identical copy of the source folder in the replica folder. It performs one-way synchronization, where the content of the replica folder is modified to match the content of the source folder.

## Features

- Periodic one-way synchronization of folders.
- Logging of file creation, copying, and removal operations.
- Customizable synchronization interval and log file path.
- Command-line interface for easy setup and configuration.

## Usage
To use the script, run it from the command line with the following arguments:

python folder_sync.py <source_path> <replica_path> <sync_interval_seconds> <log_file>

Command-Line Arguments
<source_path> (required): The source folder path.
<replica_path> (required): The replica folder path.
<sync_interval_seconds> (required): The synchronization interval in seconds.
<log_file> (required): The path to the log file.

## Logging
File creation, copying, and removal operations are logged to both the console and the specified log file. Log messages include timestamps for easy reference.
