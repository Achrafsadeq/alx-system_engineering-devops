 # 0x08. Networking basics #1

## Description
This project focuses on essential networking concepts in a Unix environment. The tasks introduce you to configuring hostnames, understanding localhost, managing network interfaces, and using various network tools to display and debug IP configurations. By the end of this project, you will have a solid understanding of networking basics and be able to execute and interpret network commands effectively.

## Requirements
| **Category**         | **Details**                                        |
|----------------------|----------------------------------------------------|
| **Editors**          | `vi`, `vim`, `emacs`                               |
| **Operating System** | Ubuntu 20.04 LTS                                   |
| **File Endings**     | All files should end with a new line               |
| **README**           | A `README.md` file at the root of the project folder is mandatory |
| **Bash Scripts**     | All Bash scripts must be executable                |
| **Shellcheck**       | Scripts must pass Shellcheck (version 0.7.0) without errors |
| **Shebang**          | All scripts should start with `#!/usr/bin/env bash` |
| **Script Comments**  | The second line of each script should describe its purpose |

### Bash Script Guidelines
- Ensure all scripts are tested and function as intended.
- Always include comments for clarity and to explain complex logic.
- Follow Shellcheck standards to ensure quality and maintainability.

## Learning Objectives
By the end of this project, you will be able to:
- Explain what `localhost` and `127.0.0.1` represent.
- Describe the purpose of `0.0.0.0`.
- Understand the significance of `/etc/hosts`.
- Display your machine's active network interfaces.
- Utilize networking tools to debug and monitor network issues.

## Tasks
| **Task** | **Description**                                      | **File**                         |
|----------|------------------------------------------------------|----------------------------------|
| **0**    | Write a script to change your home IP configuration. | `0-change_your_home_IP`          |
| **1**    | Write a script to show all active IPv4 IPs.          | `1-show_attached_IPs`            |
| **2**    | [Advanced] Create a script to listen on port 98.     | `100-port_listening_on_localhost` |

## Detailed Task Descriptions
### Task 0: Change your home IP
- **Description**: Write a Bash script that modifies your Ubuntu server's IP settings such that `localhost` resolves to `127.0.0.2` and `facebook.com` resolves to `8.8.8.8`.
- **Example**: Run `ping localhost` and `ping facebook.com` before and after executing the script to observe the changes.
- **File**: `0-change_your_home_IP`

### Task 1: Show attached IPs
- **Description**: Create a script that lists all active IPv4 addresses on your system.
- **Example**: The output will show both `127.0.0.1` and your machine's IP.
- **File**: `1-show_attached_IPs`

### Task 2: Port listening on localhost (Advanced)
- **Description**: Write a Bash script that listens on port 98 and echoes received data. Test it using `telnet`.
- **Example**: Establish a telnet connection to `localhost` on port 98 and exchange data.
- **File**: `100-port_listening_on_localhost`
  
## Author
**Codename**: Achraf Sadeq

## Acknowledgments
Developed as part of the ALX Software Engineering Program in collaboration with Holberton School.

