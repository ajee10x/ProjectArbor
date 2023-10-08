#!/bin/bash

# Set the GitHub username and repository name that you want to make a project tree for it
USERNAME="Any_GitHub_Username"
REPO="Any_GitHub_Repository_Name"

# Set your Github personal access token
TOKEN="Your_Github_Personal_Access_Token"

# Output file for saving file and directory names
OUTPUT_FILE="github_project_tree.txt"

# Function to fetch file and directory names recursively
fetch_files_and_directories() {
    local url="$1"
    local indent="$2"

    # Fetch the list of files and directories from the GitHub API
    local response
    if [ -n "$TOKEN" ]; then
        response=$(curl -s -H "Authorization: token $TOKEN" "$url")
    else
        response=$(curl -s "$url")
    fi

    # Process the response to extract file and directory names
    local entries=$(echo "$response" | jq -r '.[] | .name')

    # Output the items with appropriate indentation, filtering out invalid characters
    for entry in $entries; do
        # Check if the entry contains any control characters or invalid characters
        if [[ "$entry" =~ [[:cntrl:]] || "$entry" =~ [[:space:]] ]]; then
            continue
        fi

        # Check if the entry is a directory
        local is_directory=$(echo "$response" | jq -r ".[] | select(.name == \"$entry\") | .type")

        if [ "$is_directory" = "dir" ]; then
            # If it's a directory, create a corresponding entry in the output
            echo "${indent}    ├── $entry" >> "$OUTPUT_FILE"
            # Recursively fetch files and directories within this directory
            fetch_files_and_directories "$url/$entry" "$indent    │"
        else
            # If it's a file, create an entry without the trailing "/"
            echo "${indent}    └── $entry" >> "$OUTPUT_FILE"
        fi
    done
}

# Initialize the output file
echo "## Project Directory/Structure/Tree \n    ." > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Start fetching files and directories for the root directory
fetch_files_and_directories "https://api.github.com/repos/$USERNAME/$REPO/contents" ""

echo "Project structure saved in $OUTPUT_FILE"
