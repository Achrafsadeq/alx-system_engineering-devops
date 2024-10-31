# 0x04. Loops, Conditions and Parsing

## Description

This project focuses on Bash scripting fundamentals, specifically the use of loops, conditionals, and parsing in shell scripts. By working through these tasks, you'll gain experience with Bash scripting structures, handling conditions, and writing scripts that process and manipulate text.

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
* Loops, conditional statements, and functions should follow best practices for readability and efficiency.
* Avoid using `awk` for this project, as tasks focus on basic shell utilities.

## Tasks

| Task Number | Description                                                          | File Name               |
|-------------|----------------------------------------------------------------------|--------------------------|
| 0           | Create an RSA key pair for SSH authentication.                       | `0-RSA_public_key.pub`  |
| 1           | Write a script that displays "Best School" 10 times using a `for` loop. | `1-for_best_school`      |
| 2           | Write a script that displays "Best School" 10 times using a `while` loop. | `2-while_best_school`  |
| 3           | Write a script that displays "Best School" 10 times using an `until` loop. | `3-until_best_school`  |
| 4           | Write a script that displays "Best School" and adds "Hi" on the 9th iteration. | `4-if_9_say_hi`     |
| 5           | Write a script that loops from 1 to 10, displaying "bad luck" for the 4th and "good luck" for the 8th iterations. | `5-4_bad_luck_8_is_your_chance` |
| 6           | Write a script that displays numbers from 1 to 20, with unique messages for specific numbers. | `6-superstitious_numbers` |
| 7           | Write a script to display a 12-hour and 59-minute time format using nested loops. | `7-clock`            |
| 8           | Write a script that lists the contents of the directory, only showing names after the first dash. | `8-for_ls`           |
| 9           | Write a Bash script that gives information about the school file.  | `9-to_file_or_not_to_file`           |
| 10          | Write a Bash script that displays numbers from 1 to 100. | `10-fizzbuzz`           |

## Advanced Tasks

| Task Number | Description                                                          | File Name               |
|-------------|----------------------------------------------------------------------|--------------------------|
| 100         | Write a script that tells a story based on the contents of `/etc/passwd`. | `100-read_and_cut`  |
| 101         | Parse and display specific fields of each line in `/etc/passwd` in a formatted way. | `101-tell_the_story_of_passwd` |
| 102         | Write a Bash script that displays the visitor IP and HTTP status code from an Apache log file. | `102-lets_parse_apache_logs` |
| 103         | Using the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, displaying this data in descending order of occurrences.  | `103-dig_the-data` |

## Learning Objectives

By the end of this project, you will be able to:

* Use `for`, `while`, and `until` loops in Bash scripts.
* Implement conditional statements with `if`, `elif`, and `else`.
* Utilize `case` statements for pattern matching and structured decision-making.
* Parse and manipulate text output with `cut`, `grep`, and redirection operators.
* Write robust Bash scripts that pass Shellcheck validation.

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
 Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.

