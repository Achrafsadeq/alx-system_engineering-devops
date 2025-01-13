# 0x0D-web_stack_debugging_0

## Background Context

This project focuses on debugging a web stack to ensure that a web server (Apache) runs correctly inside a Docker container and serves a "Hello ALX" page when queried. Debugging is a critical skill in software engineering, and this project will help you understand how to diagnose and fix issues in a web server environment.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Docker Version** | Docker 20.10+ |
| **Apache Version** | Apache 2.4.7 (Ubuntu 14.04 LTS) |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Bash scripts must end with `.sh` |

## General Requirements

1. **Bash Scripts**: All Bash scripts must be executable and pass `shellcheck` without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Bash script must be a comment explaining its purpose.
3. **Ubuntu 14.04 LTS**: All files will be interpreted on Ubuntu 14.04 LTS.
4. **Apache Configuration**: Apache should be configured to listen on port 80 and serve a custom "Hello ALX" page.

### Docker Installation Guide

1. Ensure Docker is installed:
   ```bash
   $ sudo apt-get install docker.io
   ```

2. Verify the installation:
   ```bash
   $ docker --version
   ```

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. Give me a page!**        | Debug and fix an Apache web server running in a Docker container to serve a "Hello ALX" page | `0-give_me_a_page` |

## Learning Objectives

By completing this project, you will:

- Understand the basics of Docker and containerization.
- Learn how to debug a web server running inside a Docker container.
- Gain experience with Apache configuration and troubleshooting.
- Develop problem-solving skills in a real-world debugging scenario.

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x0D-web_stack_debugging_0`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.

