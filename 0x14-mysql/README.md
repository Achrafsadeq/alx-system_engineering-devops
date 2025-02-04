# 0x14. MySQL


## Background Context

This project focuses on setting up and managing MySQL databases, including replication and backups. By completing this project, you will gain hands-on experience with MySQL configuration, user management, replication, and backup strategies.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **MySQL Version** | MySQL 5.7.x (Ubuntu 16.04 LTS) |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Bash scripts must end with `.sh` |

## General Requirements

1. **Bash Scripts**: All Bash scripts must be executable and pass `shellcheck` without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Bash script must be a comment explaining its purpose.
3. **Ubuntu 16.04 LTS**: All files will be interpreted on Ubuntu 16.04 LTS.
4. **MySQL Configuration**: MySQL must be properly configured and running on both `web-01` and `web-02` servers.

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|---------------------------------------------|-------------------------------|
| **0. Install MySQL**          | Install MySQL 5.7.x on both `web-01` and `web-02` servers | `0-install_mysql` |
| **1. Let us in!**             | Create a MySQL user `holberton_user` with the required permissions | `1-create_user` |
| **2. If only you could see what I've seen with your eyes** | Create a database `tyrell_corp` and a table `nexus6` with at least one entry | `2-create_database` |
| **3. Quite an experience to live in fear, isn't it?** | Create a MySQL user `replica_user` with replication permissions | `3-create_replica_user` |
| **4. Setup a Primary-Replica infrastructure using MySQL** | Configure MySQL primary on `web-01` and replica on `web-02` | `4-mysql_configuration_primary`, `4-mysql_configuration_replica` |
| **5. MySQL backup**           | Write a Bash script to generate a MySQL dump and compress it into a `.tar.gz` archive | `5-mysql_backup` |


## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x14-mysql`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.


