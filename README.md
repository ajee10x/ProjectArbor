# ProjectArbor Version 2.0.0

![Alt text](/screenshots/logo_v_2_0_0.png?raw=true "logo")



## About

ProjectArbor is a tool for generating project directory structures in a tree format for any Github repository or any Local project directory, it allows you to visualize and organize your project's files and directories in a tree-like structure.
The best part about this tool, all you need to do is to copy and paste directily into your `README.md` file without any editing on the output that you scrapped, and it will apear at the desired shape that you want.



## Table of Contents

- [About](#about)
- [What's new in Version 2.0.0 ?](#whatnew)
- [Getting Started](#getting-started)
  - [Prerequisites for Linux](#prerequisites-for-linux)
  - [Prerequisites for Windows](#prerequisites-for-windows)
- [Installation](#installation)
  - [Installation for Linux](#installation-for-linux)
  - [Installation for Windows](#installation-for-windows)
- [Usage](#usage)
  - [Github Arbor Builder Usage](#usage-github)
  - [Local Arbor Builder Usage](#usage-local)
- [Example](#example)
- [Tested](#tested)
- [Contributing](#contributing)
- [License](#license)

## What's new in Version 2.0.0 ?
- Converted the whole project from shell script to python.
- Works on windows also.
- Easy use and friendly terminal interface.
- Log supported and previous configurations


## Getting Started


### Prerequisites for Linux

Before you get started, make sure you have the following prerequisites:

- python3
- jq (a lightweight and flexible command-line JSON processor)

You can install `jq` using your package manager. For example, on Linux:
```console
sudo apt-get install jq
```
```console
pip install -r requirements.txt
```

### Prerequisites for Windows

Before you get started, make sure you have the following prerequisites:

- python3

```console
pip install -r requirements.txt
```

## Installation


- Clone this repository to your local machine:
```console
git clone https://github.com/ajee10x/ProjectArbor.git
cd ProjectArbor
```

### Installation for Linux

- For Linux - Make the pythonfiles executable:
```console
chmod +x ArborBuilder.py
chmod +x LocalArborBuilder.py
```

- or using this command to make the project files executable
```console
chmod +x *
```

### Installation for Windows

```console
Nothing to worry about :)
```

## Usage


### Github Arbor Builder Usage

To generate a project tree structure for a GitHub any repository:

- Run the Following command:
```console
python ArborBuilder.py
```
- Enter a username that you want to have their repo projects tree, for example we will use `github`:
```console
 _____           _         _   _____     _
|  _  |___ ___  |_|___ ___| |_|  _  |___| |_ ___ ___  v2.0.0
|   __|  _| . | | | -_|  _|  _|     |  _| . | . |  _|
|__|  |_| |___|_| |___|___|_| |__|__|_| |___|___|_|
              |___|
                                                                                                                        


Previous Configurations:
1. ajee10x
2. torvalds
Enter the number to select a username or 0 for new input: 0
Enter your GitHub username: github
```

- Set your Github personal access token from https://github.com/settings/tokens

- Now, after generating a token, copy it and paste it into the command line then hit enter:

```console
Previous Tokens:
1. My_Old_Github_Personal_Access_Token
Enter the number to select a token or 0 for new input: 0
Enter the new token: Your_Github_Personal_Access_Token
```

In case you faced a problems with it, just paste it into that file `GithubTokens.config`

- Now, you can see Public Repositories for any Github username that you entered:

```console
Public Repositories for github:
1. .github
2. accessibility-alt-text-bot
3. accessibilityjs
4. actions-cheat-sheet
5. actions-learning-pathway
6. actions-oidc-debugger
7. actions-oidc-gateway-example
8. advisory-database
9. AFNetworking
10. albino
11. aptly
12. Archimedes
13. archive-program
14. argo-ml
15. aroma
16. auto-check-element
17. auto-complete-element
18. automatic-contrib-prs
19. aws-s3
20. azure-quickstart-templates
21. babel-plugin-ensure-name-for-custom-elements
22. babel-plugin-transform-custom-element-classes
23. babel-plugin-transform-invariant-location
24. babel-preset-github
25. backstop
26. backup-utils
27. balanced-employee-ip-agreement
28. banana_phone
29. bellevue-murals
30. bert
Enter the number to select a repository or 0 for new input: 28
Project structure saved in github_project_tree.txt
```

This script fetches the HTML content of the repository page and then uses grep, cut, and sed to extract the file and directory names.

- Now you will find the tree project in that folder:
`github_project_tree.txt`


### Local Arbor Builder Usage

You can also generate a project tree structure for a local directory before uploading your project on github on your computer using `LocalArborBuilder.py`.



- After editing, now run the following command:
```console
python LocalArborBuilder.py
```

- Now select which platform you are using at the moment:

```console
 _____           _         _   _____     _
|  _  |___ ___  |_|___ ___| |_|  _  |___| |_ ___ ___  v2.0.0
|   __|  _| . | | | -_|  _|  _|     |  _| . | . |  _|
|__|  |_| |___|_| |___|___|_| |__|__|_| |___|___|_|
              |___|
                                                                                                                        


Select the platform:
1. linux
2. windows
Enter the platform number (1 or 2): 2
```

- After that, you can find prevoise projects path or paste a new one:
```console
Previous Paths:
1. C:\Users\demo\Desktop\ProjectArbor-main
2. Enter a new path
Enter the number to select a previous path or enter a new one: 2
```
- Now, enter a new path:
```console
Enter the path to your local project folder: C:\Users\demo\Desktop\banana_phone-master
Local project structure saved in local_project_tree.txt
```
This will create a 'local_project_tree.txt' file containing the local project tree structure.

- Now you will find the tree project in that folder:
`local_project_tree.txt`

## Example
- This was a live(github)  and local tested on that project https://github.com/github/banana_phone

## Project Directory/Structure/Tree 
    .

    └── .gitignore
    └── Gemfile
    └── Gemfile.lock
    └── LICENSE
    └── README.md
    └── Rakefile
    └── banana_phone.gemspec
    ├── lib
    │    └── banana_phone.rb
    │    ├── banana_phone
    │    │    └── action.rb
    │    │    └── encodes.rb
    │    │    └── errors.rb
    │    │    └── mod.rb
    │    │    └── request.rb
    │    │    └── service.rb
    ├── test
    │    └── action_test.rb
    │    └── encodes_test.rb
    │    └── error_test.rb
    │    └── mod_test.rb
    │    └── request_test.rb
    │    └── service_test.rb
    │    └── test_helper.rb




## Contributing

Contributions are welcome! If you have any ideas or improvements for ProjectArbor, please open an issue or submit a pull request.

## Tested
- [x] Windows 11
- [x] Kali Linux 2023.4


## License
This project is licensed under the MIT license - see the LICENSE file for details.
