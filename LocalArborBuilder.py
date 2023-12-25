import os

# Function to display an ASCII art banner
def print_banner():
    print(r'''                                                 
 _____           _         _   _____     _             
|  _  |___ ___  |_|___ ___| |_|  _  |___| |_ ___ ___  v2.0.0 
|   __|  _| . | | | -_|  _|  _|     |  _| . | . |  _|  
|__|  |_| |___|_| |___|___|_| |__|__|_| |___|___|_|    
              |___|                                    
                                                                                                                                                                                                                                                                                                                                             
    ''')
print_banner()

# Define the file path for storing previous paths
LOG_FILE = "LocalPath.log"

# Define the list of platform choices
platform_choices = ['linux', 'windows']

# Function to display the menu for selecting a platform
def display_platform_menu():
    print("Select the platform:")
    for i, choice in enumerate(platform_choices, start=1):
        print(f"{i}. {choice}")

# Function to get user input for platform choice
def get_platform_choice():
    return int(input("Enter the platform number (1 or 2): ")) - 1

# Function to get user input for the local project folder path
def get_local_path():
    return input("Enter the path to your local project folder: ")

# Function to save the entered path to the log file
def save_to_log(path):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(path + "\n")

# Function to display previous paths and get user input for selection
def select_previous_path():
    print("Previous Paths:")
    with open(LOG_FILE, "r") as log_file:
        previous_paths = log_file.readlines()
        for i, path in enumerate(previous_paths, start=1):
            print(f"{i}. {path.strip()}")

    print(f"{len(previous_paths)+1}. Enter a new path")

    choice = int(input("Enter the number to select a previous path or enter a new one: "))
    if choice == len(previous_paths) + 1:
        return get_local_path()
    elif choice in range(1, len(previous_paths) + 1):
        return previous_paths[choice - 1].strip()
    else:
        print("Invalid choice. Exiting.")
        exit()

# Check if the log file exists, if not create an empty one
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'a').close()

# Get user input for the platform choice
display_platform_menu()
platform_choice_index = get_platform_choice()

# Validate the user's input
if platform_choice_index not in range(len(platform_choices)):
    print("Invalid platform choice. Exiting.")
    exit()

# Map the user's choice to the corresponding platform
platform_choice = platform_choices[platform_choice_index]

# Get user input for the local project folder path
LOCAL_PATH = select_previous_path()

# Save the entered path to the log file
save_to_log(LOCAL_PATH)

# Normalize the path separator based on the platform
if platform_choice == 'windows':
    LOCAL_PATH = LOCAL_PATH.replace('/', '\\')
elif platform_choice == 'linux':
    LOCAL_PATH = LOCAL_PATH.replace('\\', '/')

# Output file for saving file and directory names
OUTPUT_FILE = "local_project_tree.txt"

# Function to fetch file and directory names recursively
def fetch_files_and_directories(path, indent):
    # Process the files and directories in the current directory
    for entry in os.listdir(path):
        # Extract the name of the entry
        entry_path = os.path.join(path, entry)
        entry_name = os.path.basename(entry_path)

        # Check if the entry is a directory
        if os.path.isdir(entry_path):
            # If it's a directory, create a corresponding entry in the output
            with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
                file.write(f"{indent}    ├── {entry_name}\n")
            # Recursively fetch files and directories within this directory
            fetch_files_and_directories(entry_path, f"{indent}    │")
        else:
            # If it's a file, create an entry without the trailing "/"
            with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
                file.write(f"{indent}    └── {entry_name}\n")

# Initialize the output file
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write("## Project Directory/Structure/Tree \n    .\n\n")

# Start fetching files and directories for the root directory
fetch_files_and_directories(LOCAL_PATH, "")

print(f"Local project structure saved in {OUTPUT_FILE}")
