# Attack is the Best Defense

## Background Context

This project focuses on understanding and applying network security concepts, including ARP spoofing, sniffing unencrypted traffic, and performing dictionary attacks. By completing this project, you will gain hands-on experience in identifying vulnerabilities in network communication and exploiting them to understand how attackers can compromise systems. This knowledge will help you build more secure systems in the future.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Advanced |
| **Review**       | Manually reviewed by peers or TAs |
| **Tools**        | `tcpdump`, `hydra`, Docker |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Bash scripts must end with `.sh` |

## General Requirements

1. **Bash Scripts**: All Bash scripts must be executable and pass `shellcheck` without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Bash script must be a comment explaining its purpose.
3. **Ubuntu 14.04 LTS**: All files will be interpreted on Ubuntu 14.04 LTS.
4. **Network Tools**: Use tools like `tcpdump` and `hydra` to perform network analysis and attacks.

---

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. ARP spoofing and sniffing unencrypted traffic** | Sniff unencrypted traffic to extract sensitive information (e.g., passwords) | `0-sniffing` |
| **1. Dictionary attack**      | Perform a dictionary attack on an SSH account using `hydra` | `1-dictionary_attack` |

---

## Learning Objectives

By completing this project, you will:

- Understand the risks of unencrypted network traffic.
- Learn how to use `tcpdump` to sniff network traffic.
- Gain experience with ARP spoofing and its implications.
- Perform a dictionary attack using `hydra` to brute-force SSH credentials.
- Develop skills to identify and mitigate network security vulnerabilities.

---

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `attack_is_the_best_defense`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.

