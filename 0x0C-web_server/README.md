# 0x0C-web_server

## Background Context

This project focuses on learning and applying web server configuration and management using Nginx. Nginx is a high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server. By completing this project, you will gain hands-on experience with Nginx installation, configuration, domain setup, redirection, and custom error pages.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Nginx Version** | Nginx 1.4.6 (Ubuntu) |
| **Puppet Version** | Puppet 5.5 (for advanced tasks) |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Bash scripts must end with `.sh` and Puppet manifests with `.pp` |

## General Requirements

1. **Bash Scripts**: All Bash scripts must be executable and pass `shellcheck` without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Bash script must be a comment explaining its purpose.
3. **Ubuntu 20.04 LTS**: All files will be interpreted on Ubuntu 20.04 LTS.
4. **Nginx Configuration**: Nginx should be configured to listen on port 80 and serve a custom "Hello World!" page.

### Nginx Installation Guide

1. Ensure Nginx is installed:
   ```bash
   $ sudo apt-get install nginx
   ```

2. Verify the installation:
   ```bash
   $ nginx -v
   ```

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. Transfer a file to your server** | Write a Bash script to transfer a file to a server using SCP | `0-transfer_file` |
| **1. Install Nginx web server** | Write a Bash script to install and configure Nginx on a server | `1-install_nginx_web_server` |
| **2. Setup a domain name**     | Configure a domain name to point to your server | `2-setup_a_domain_name` |
| **3. Redirection**             | Configure Nginx to redirect a specific path to another URL | `3-redirection` |
| **4. Not found page 404**      | Configure Nginx to serve a custom 404 error page | `4-not_found_page_404` |
| **5. Install Nginx web server (w/ Puppet)** | Use Puppet to install and configure Nginx | `7-puppet_install_nginx_web_server.pp` |

## Learning Objectives

By completing this project, you will:

- Understand the basics of Nginx and its configuration.
- Learn how to install and configure a web server.
- Gain experience with domain name setup and DNS configuration.
- Configure redirection and custom error pages in Nginx.
- Automate web server configuration tasks using Puppet.

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x0C-web_server`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.
