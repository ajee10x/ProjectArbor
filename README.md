# ProjectArbor Version 1.0

![Alt text](/screenshots/logo.png?raw=true "logo")

## About

ProjectArbor is a tool for generating project directory structures in a tree format for any Github repository or any Local project directory, it allows you to visualize and organize your project's files and directories in a tree-like structure.
The best part about this tool, all you need to do is to copy and paste directily into your `README.md` file without any editing on the output that you scrapped, and it will apear at the desired shape that you want.


## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Github Arbor Builder Usage](#usage-github)
  - [Local Arbor Builder Usage](#usage-local)
- [Example](#example)
- [Contributing](#contributing)
- [Tested](#tested)
- [License](#license)


## Getting Started


### Prerequisites

Before you get started, make sure you have the following prerequisites:

- Bash shell
- jq (a lightweight and flexible command-line JSON processor)

You can install `jq` using your package manager. For example, on Linux:
```console
sudo apt-get install jq
```


### Installation


- Clone this repository to your local machine:
```console
git clone https://github.com/ajee10x/ProjectArbor.git
cd ProjectArbor
```


- Make the shell scripts executable:
```console
chmod +x ArborBuilder.sh
chmod +x LocalArborBuilder.sh
```

- or using this command to make the shell scripts executable
```console
chmod +x *
```


## Usage


### Github Arbor Builder Usage

To generate a project tree structure for a GitHub any repository:

- Open the `ArborBuilder.sh` file and edit the following:

- Change the following values at your desire:
`USERNAME="Any_GitHub_Username"`
`REPO="Any_GitHub_Repository_Name"`

- Set your Github personal access token from https://github.com/settings/tokens
`TOKEN="Your_Github_Personal_Access_Token"`

- After editing, now run the following command:
```console
sh ArborBuilder.sh
```
or

```console
./ArborBuilder.sh
```

This script fetches the HTML content of the repository page and then uses grep, cut, and sed to extract the file and directory names.

- Now you will find the tree project in that folder:
`github_project_tree.txt`


### Local Arbor Builder Usage

You can also generate a project tree structure for a local directory before uploading your project on github on your computer using 'LocalArborBuilder.sh'.

Open the `LocalArborBuilder.sh` file and edit the following:

- Change the following values at your desire:
`LOCAL_PATH="Your_Porject_Folder_Path"`

- After editing, now run the following command:
```console
sh LocalArborBuilder.sh
```
or

```console
./LocalArborBuilder.sh
```
This will create a 'local_project_tree.txt' file containing the local project tree structure.

- Now you will find the tree project in that folder:
`local_project_tree.txt`

## Example
- This was a live(github) and local tested on that project https://github.com/ajee10x/LTM-LinuxTaskManager

## Project Directory/Structure/Tree
    .

    └── LICENSE
    └── LTM.jar
    └── README.md
    ├── bin
    │    └── jfreechart.jar
    │    ├── ltm
    │    │    └── AppHistoryPanel$1.class
    │    │    └── AppHistoryPanel$AppLaunchInfo.class
    │    │    └── AppHistoryPanel.class
    │    │    └── DetailsPanel.class
    │    │    └── Main.class
    │    │    └── PerformancePanel.class
    │    │    └── ProcessesPanel$1.class
    │    │    └── ProcessesPanel$2.class
    │    │    └── ProcessesPanel.class
    │    │    └── ServicesPanel.class
    │    │    └── StartupPanel$1.class
    │    │    └── StartupPanel$2.class
    │    │    └── StartupPanel$3.class
    │    │    └── StartupPanel$4.class
    │    │    └── StartupPanel$5.class
    │    │    └── StartupPanel$6.class
    │    │    └── StartupPanel.class
    │    │    └── UsersPanel.class
    │    │    ├── scripts
    │    │    │    └── app_history.sh
    │    │    │    └── details.sh
    │    │    │    └── list_running_processes.sh
    │    │    │    └── performance_data.sh
    │    │    │    └── services_data.sh
    │    │    │    └── set_execute_permission.sh
    │    │    │    └── startup_data.sh
    │    │    │    └── system_details.sh
    │    │    │    └── user_data.sh
    ├── screenshots
    │    └── ApplicationHistory.jpg
    │    └── PCdetials.jpg
    │    └── Process.jpg
    │    └── ServiceControl.jpg
    │    └── StartupApplications.jpg
    │    └── SystemPerformanceMonitoring.jpg
    │    └── UserManagement.jpg
    │    └── ltmlogo.jpg
    │    └── ltmlogo_50.jpg
    ├── src
    │    └── jfreechart.jar
    │    ├── ltm
    │    │    └── AppHistoryPanel.java
    │    │    └── DetailsPanel.java
    │    │    └── LTMApplication.java
    │    │    └── Main.java
    │    │    └── PerformancePanel.java
    │    │    └── ProcessesPanel.java
    │    │    └── ServicesPanel.java
    │    │    └── StartupPanel.java
    │    │    └── UsersPanel.java
    │    │    ├── scripts
    │    │    │    └── app_history.sh
    │    │    │    └── details.sh
    │    │    │    └── list_running_processes.sh
    │    │    │    └── performance_data.sh
    │    │    │    └── services_data.sh
    │    │    │    └── set_execute_permission.sh
    │    │    │    └── startup_data.sh
    │    │    │    └── system_details.sh
    │    │    │    └── user_data.sh
    └── version.txt



## Contributing

Contributions are welcome! If you have any ideas or improvements for ProjectArbor, please open an issue or submit a pull request.

## Tested
- [x] Kali Linux 2023.3

## License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
