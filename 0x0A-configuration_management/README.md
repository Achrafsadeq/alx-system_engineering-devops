# 0x0A-configuration_management (Configuration Management with Puppet)

## Background Context

This project focuses on learning and applying configuration management using Puppet. Puppet is a powerful tool for automating the management of infrastructure, ensuring consistency, and reducing manual intervention. By completing this project, you will gain hands-on experience with Puppet manifests, resource management, and basic automation tasks.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Puppet Version** | Puppet 5.5 |
| **Puppet-lint Version** | 2.1.1 |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Puppet manifests must end with `.pp` |

## General Requirements

1. **Puppet Manifests**: All Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Puppet manifest must be a comment explaining its purpose.
3. **Ubuntu 20.04 LTS**: All files will be interpreted on Ubuntu 20.04 LTS.
4. **Puppet Installation**: Puppet 5.5 is preinstalled on the Ubuntu 20.04 VM.

### Puppet Installation Guide

1. Install Puppet and required dependencies:
   ```bash
   $ apt-get install -y ruby=1:2.7+1 --allow-downgrades
   $ apt-get install -y ruby-augeas
   $ apt-get install -y ruby-shadow
   $ apt-get install -y puppet
   ```

2. Install `puppet-lint`:
   ```bash
   $ gem install puppet-lint
   ```

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. Create a file**          | Create a file in `/tmp` with specific permissions and content | `0-create_a_file.pp` |
| **1. Install a package**      | Install `flask` from `pip3` with a specific version | `1-install_a_package.pp` |
| **2. Execute a command**      | Create a manifest that kills a process named `killmenow` | `2-execute_a_command.pp` |

## Learning Objectives

By completing this project, you will:

- Understand the basics of Puppet and its syntax.
- Learn how to create and manage Puppet manifests.
- Gain experience with resource management in Puppet.
- Automate tasks such as file creation, package installation, and process management.

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x0A-configuration_management`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School in collaboration with the ALX Software Engineering Program to provide hands-on learning in a professional environment.
