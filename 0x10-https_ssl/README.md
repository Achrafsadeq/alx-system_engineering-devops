# 0x10. HTTPS SSL

## Background Context

This project focuses on configuring HTTPS and SSL for secure web traffic. By completing this project, you will gain hands-on experience with SSL certificates, HAProxy SSL termination, and enforcing HTTPS traffic. You will also learn how to automate domain and subdomain configurations using Bash scripts.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **HAProxy Version** | HAProxy 1.5 or higher (Ubuntu 16.04 LTS) |
| **Certbot**      | Used for generating SSL certificates |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Bash scripts must end with `.sh` |

## General Requirements

1. **Bash Scripts**: All Bash scripts must be executable and pass `shellcheck` (version 0.3.7) without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Bash script must be a comment explaining its purpose.
3. **Ubuntu 16.04 LTS**: All files will be interpreted on Ubuntu 16.04 LTS.
4. **SSL Configuration**: HAProxy must be configured to handle SSL termination and enforce HTTPS traffic.

## Learning Objectives

By completing this project, you will:

- Understand the roles of HTTPS and SSL in securing web traffic.
- Learn how to configure SSL termination on HAProxy.
- Gain experience with generating SSL certificates using Certbot.
- Automate domain and subdomain configurations using Bash scripts.
- Enforce HTTPS traffic to ensure secure communication.

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. World wide web**         | Configure subdomains and write a Bash script to display subdomain information | `0-world_wide_web` |
| **1. HAproxy SSL termination** | Configure HAProxy to handle SSL termination for your subdomain `www` | `1-haproxy_ssl_termination` |
| **2. No loophole in your website traffic** | Configure HAProxy to redirect HTTP traffic to HTTPS | `100-redirect_http_to_https` |

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x10-https_ssl`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.
