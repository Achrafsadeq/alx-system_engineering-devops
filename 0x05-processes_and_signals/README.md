# 0x05. Processes and Signals

## Description

This project focuses on understanding and working with processes and signals in a Unix-like environment. You'll learn how to handle process IDs, send signals, and use tools for process control in Bash scripts. Through these tasks, you’ll gain experience in managing process states, utilizing signals, and working with basic system calls.

## Requirements

| Category                | Details                                                  |
|-------------------------|----------------------------------------------------------|
| Editors                 | `vi`, `vim`, `emacs`                                     |
| Interpreter             | Ubuntu 20.04 LTS                                         |
| File Endings            | All files should end with a new line                     |
| README                  | A `README.md` file at the root of the project folder is mandatory |
| Coding Style            | All Bash scripts must pass Shellcheck (version 0.7.0)    |
| Script Permissions      | All Bash scripts must be executable                      |
| Header Line             | `#!/usr/bin/env bash`                                    |
| Global Variables        | Not allowed                                              |
| Comment Requirement     | Second line of all scripts must explain the script's function |

## Bash Scripting Guidelines

* All Bash scripts must start with `#!/usr/bin/env bash`.
* Shellcheck must pass without any error for all scripts.
* Use best practices for readability and efficiency, especially when handling process and signal-related commands.
* Avoid complex commands unless necessary to fulfill task requirements.

## Tasks

| Task Number | Description                                                          | File Name               |
|-------------|----------------------------------------------------------------------|--------------------------|
| 0           | Write a script that displays its own PID.                            | `0-what-is-my-pid`      |
| 1           | Write a script that lists currently running processes for all users. | `1-list_your_processes` |
| 2           | Write a script that displays the PID of a given process name.        | `2-show_pid`            |
| 3           | Write a script that creates a process that sleeps indefinitely.      | `3-infinite_loop`       |
| 4           | Write a script that kills a process by PID.                          | `4-kill_me_now`         |
| 5           | Write a script that kills multiple instances of a process by name.   | `5-kill_me_now_again`   |
| 6           | Write a script to use signals to stop and continue a process.        | `6-signal_me`           |
| 7           | Write a script to handle `SIGTERM` signal with a message.            | `7-stop_me_if_you_can`  |
| 8           | Write a script to catch and report specific signals for a process.   | `8-catch_me_if_you_can` |

## Advanced Tasks

| Task Number | Description                                                          | File Name               |
|-------------|----------------------------------------------------------------------|--------------------------|
| 100         | Write a script that listens for specific signals and logs them.      | `100-signal_listener`   |
| 101         | Implement a script that restarts itself upon receiving `SIGHUP`.     | `101-reload_me`         |
| 102         | Write a script that creates a process tree view of running processes.| `102-process_tree`      |

## Learning Objectives

By the end of this project, you will be able to:

* Retrieve and use process IDs with `ps` and other commands.
* Send signals to processes and handle them within scripts.
* Create and manage background processes.
* Use Shellcheck to ensure all scripts adhere to best practices.
* Develop scripts that handle specific system signals to control process behavior.

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
 Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
