# 0x12. Web Stack Debugging #2

## Background Context

This project focuses on debugging and fixing issues in a web stack environment. By completing this project, you will gain hands-on experience with running software as a different user, configuring services to run under specific users, and writing efficient Bash scripts to solve problems. You will also learn how to debug and secure web servers like Nginx.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Environment**  | Ubuntu 20.04 LTS |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Bash scripts must end with `.sh` |

## General Requirements

1. **Bash Scripts**: All Bash scripts must be executable and pass `shellcheck` (version 0.3.7) without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Bash script must be a comment explaining its purpose.
3. **Ubuntu 20.04 LTS**: All files will be interpreted on Ubuntu 20.04 LTS.
4. **Script Execution**: Your Bash scripts must run without errors and meet the specified requirements.


## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. Run software as another user** | Write a Bash script that runs the `whoami` command under a specified user | `0-iamsomeoneelse` |
| **1. Run Nginx as Nginx**      | Configure Nginx to run as the `nginx` user and listen on port 8080 | `1-run_nginx_as_nginx` |
| **2. 7 lines or less**         | Fix the Nginx configuration in 7 lines or less | `100-fix_in_7_lines_or_less` |

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x12-web_stack_debugging_2`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.
