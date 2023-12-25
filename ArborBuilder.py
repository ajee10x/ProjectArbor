import requests
import json

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

# Output file for saving file and directory names
OUTPUT_FILE = "github_project_tree.txt"
CONFIG_LOG_FILE = "GithubConfigLog.json"
TOKENS_FILE = "GithubTokens.config"

# GitHub API base URL
GITHUB_API_URL = "https://api.github.com"

# Function to fetch file and directory names recursively
def fetch_files_and_directories(url, indent):
    # Fetch the list of files and directories from the GitHub API
    headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    entries = response.json()

    # Output the items with appropriate indentation, filtering out invalid characters
    for entry in entries:
        entry_name = entry["name"]

        # Check if the entry contains any control characters or invalid characters
        if any(ord(c) < 32 or ord(c) == 127 for c in entry_name):
            continue

        # Check if the entry is a directory
        is_directory = entry["type"]

        if is_directory == "dir":
            # If it's a directory, create a corresponding entry in the output
            with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
                file.write(f"{indent}    ├── {entry_name}\n")
            # Recursively fetch files and directories within this directory
            fetch_files_and_directories(entry["url"], f"{indent}    │")
        else:
            # If it's a file, create an entry without the trailing "/"
            with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
                file.write(f"{indent}    └── {entry_name}\n")

# Function to display previous configurations and get user input for selection
def select_previous_config():
    print("Previous Configurations:")
    
    try:
        with open(CONFIG_LOG_FILE, "r") as config_file:
            previous_configs = [json.loads(line) for line in config_file if line.strip()]
    except (FileNotFoundError, json.JSONDecodeError):
        previous_configs = []

    username_dict = {}

    for config in previous_configs:
        if isinstance(config, dict):
            username = config.get("USERNAME", "Unknown")
            token_name = config.get("TOKEN_NAME", "Unknown")
            token = get_token_by_name(token_name)

            if username not in username_dict:
                # Fetch public repositories for the user
                repositories = get_public_repositories(username)
                username_dict[username] = {"TOKEN": token, "REPOS": repositories}

    for i, username in enumerate(username_dict.keys(), start=1):
        print(f"{i}. {username}")

    try:
        choice_username = int(input("Enter the number to select a username or 0 for new input: "))
        if choice_username == 0:
            return get_user_input()
        else:
            selected_username = list(username_dict.keys())[choice_username - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        exit()

    # Display public repositories as options
    print(f"Public Repositories for {selected_username}:")
    for i, repo in enumerate(username_dict[selected_username]["REPOS"], start=1):
        print(f"{i}. {repo}")

    try:
        choice_repo = int(input("Enter the number to select a repository or 0 for new input: "))
        if choice_repo == 0:
            return get_user_input()
        else:
            selected_repo = username_dict[selected_username]["REPOS"][choice_repo - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        exit()

    return {"USERNAME": selected_username, "REPO": selected_repo, "TOKEN": username_dict[selected_username]["TOKEN"]}

# Function to fetch public repositories for a GitHub user
def get_public_repositories(username):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    repositories = [repo["name"] for repo in response.json()]
    return repositories

# Function to display previous tokens and get user input for selection
def select_previous_tokens():
    print("Previous Tokens:")
    
    try:
        with open(TOKENS_FILE, "r") as tokens_file:
            tokens = [line.strip() for line in tokens_file if line.strip()]
    except FileNotFoundError:
        tokens = []

    for i, token in enumerate(tokens, start=1):
        print(f"{i}. {token}")

    try:
        choice_token = int(input("Enter the number to select a token or 0 for new input: "))
        if choice_token == 0:
            new_token = input("Enter the new token: ")
            add_token(new_token)
            return new_token
        else:
            selected_token = tokens[choice_token - 1]
            return selected_token
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        exit()

# Function to add a new token to the tokens file
def add_token(token):
    with open(TOKENS_FILE, "a") as tokens_file:
        tokens_file.write(f"{token}\n")

# Function to get a token by its name
def get_token_by_name(token_name):
    try:
        with open(TOKENS_FILE, "r") as tokens_file:
            tokens = [line.strip() for line in tokens_file if line.strip()]
        return tokens[0] if token_name in tokens else None
    except FileNotFoundError:
        return None

# Function to get user input for GitHub configuration
def get_user_input():
    username = input("Enter your GitHub username: ")
    token = select_previous_tokens()

    # Fetch live public repositories for the user
    repositories = get_public_repositories(username)

    # Display public repositories as options
    print(f"Public Repositories for {username}:")
    for i, repo in enumerate(repositories, start=1):
        print(f"{i}. {repo}")

    try:
        choice_repo = int(input("Enter the number to select a repository or 0 for new input: "))
        if choice_repo == 0:
            return get_user_input()
        else:
            selected_repo = repositories[choice_repo - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        exit()

    return {"USERNAME": username, "REPO": selected_repo, "TOKEN": token}

# Initialize the output file
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write("## Project Directory/Structure/Tree \n    .\n\n")

# Get user input for GitHub configuration
config = select_previous_config()

# Set the GitHub username, repository name, and personal access token
USERNAME = config["USERNAME"]
REPO = config["REPO"]
TOKEN = config["TOKEN"]

# Save the entered configuration to the log file
with open(CONFIG_LOG_FILE, "a") as config_file:
    json.dump(config, config_file)
    config_file.write("\n")

# Start fetching files and directories for the root directory
fetch_files_and_directories(f"{GITHUB_API_URL}/repos/{USERNAME}/{REPO}/contents", "")

print(f"Project structure saved in {OUTPUT_FILE}")
