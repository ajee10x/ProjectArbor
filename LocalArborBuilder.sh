#!/bin/bash

# Set the path to the root directory of your local project
LOCAL_PATH="Your_Porject_Folder_Path"

# Output file for saving file and directory names
OUTPUT_FILE="local_project_tree.txt"

# Function to fetch file and directory names recursively
fetch_files_and_directories() {
    local path="$1"
    local indent="$2"

    # Process the files and directories in the current directory
    for entry in "$path"/*; do
        # Extract the name of the entry
        local entry_name=$(basename "$entry")

        # Check if the entry is a directory
        if [ -d "$entry" ]; then
            # If it's a directory, create a corresponding entry in the output
            echo "${indent}    ├── $entry_name" >> "$OUTPUT_FILE"
            # Recursively fetch files and directories within this directory
            fetch_files_and_directories "$entry" "$indent    │"
        else
            # If it's a file, create an entry without the trailing "/"
            echo "${indent}    └── $entry_name" >> "$OUTPUT_FILE"
        fi
    done
}

# Initialize the output file
echo "## Project Directory/Structure/Tree \n    ." > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Start fetching files and directories for the root directory
fetch_files_and_directories "$LOCAL_PATH" ""

echo "Local project structure saved in $OUTPUT_FILE"
