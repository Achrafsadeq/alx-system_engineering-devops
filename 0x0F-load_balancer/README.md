# 0x0F. Load balancer

## Background Context

This project focuses on learning and applying load balancing concepts using HAProxy. By completing this project, you will gain hands-on experience with configuring web servers, setting up load balancers, and automating server configurations using Bash scripts.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **HAProxy Version** | HAProxy 1.6 (Ubuntu) |
| **Nginx Version** | Nginx 1.4.6 (Ubuntu) |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Bash scripts must end with `.sh` |

## General Requirements

1. **Bash Scripts**: All Bash scripts must be executable and pass `shellcheck` without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Bash script must be a comment explaining its purpose.
3. **Ubuntu 16.04 LTS**: All files will be interpreted on Ubuntu 16.04 LTS.
4. **Nginx Configuration**: Nginx should be configured to include a custom HTTP header `X-Served-By` with the server's hostname as its value.

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. Double the number of webservers** | Configure `web-02` to be identical to `web-01` and add a custom HTTP header | `0-custom_http_response_header` |
| **1. Install your load balancer** | Install and configure HAProxy on `lb-01` to distribute traffic between `web-01` and `web-02` | `1-install_load_balancer` |
| **2. Add a custom HTTP header with Puppet** | Automate the creation of a custom HTTP header using Puppet | `2-puppet_custom_http_response_header.pp` |

## Learning Objectives

By completing this project, you will:

- Understand the basics of load balancing and its importance in web infrastructure.
- Learn how to configure and manage HAProxy.
- Gain experience with automating server configurations using Bash scripts.
- Configure custom HTTP headers in Nginx.
- Automate tasks using Puppet for advanced configurations.

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x0F-load_balancer`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.

