# 0x13. Firewall

## Background Context

This project focuses on configuring and managing firewalls using `ufw` (Uncomplicated Firewall). By completing this project, you will gain hands-on experience with setting up firewall rules, blocking and allowing specific traffic, and port forwarding. You will also learn how to use `telnet` to test socket connections and debug network issues.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **ufw Version**  | `ufw` (Uncomplicated Firewall) |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Bash scripts must end with `.sh` |

## General Requirements

1. **Bash Scripts**: All Bash scripts must be executable and pass `shellcheck` (version 0.3.7) without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Bash script must be a comment explaining its purpose.
3. **Ubuntu 16.04 LTS**: All files will be interpreted on Ubuntu 16.04 LTS.
4. **Firewall Configuration**: Use `ufw` to configure firewall rules and port forwarding.
   

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. Block all incoming traffic but** | Configure `ufw` to block all incoming traffic except for SSH (port 22), HTTPS (port 443), and HTTP (port 80) | `0-block_all_incoming_traffic_but` |
| **1. Port forwarding**         | Configure `ufw` to forward port 8080/TCP to port 80/TCP | `100-port_forwarding` |

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x13-firewall`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.

