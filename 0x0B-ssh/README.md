# 0x0B-ssh

## Background Context

This project focuses on learning and applying SSH (Secure Shell) configuration and management. SSH is a cryptographic network protocol used for secure data communication, remote command-line login, and other secure network services. By completing this project, you will gain hands-on experience with SSH key management, client configuration, and automation using Puppet.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **SSH Version**  | OpenSSH 8.2p1 |
| **Puppet Version** | Puppet 5.5 (for advanced tasks) |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Bash scripts must end with `.sh` and Puppet manifests with `.pp` |

## General Requirements

1. **Bash Scripts**: All Bash scripts must be executable and pass `shellcheck` without any errors.
2. **File Structure**: All files should end with a new line, and the first line of each Bash script must be a comment explaining its purpose.
3. **Ubuntu 20.04 LTS**: All files will be interpreted on Ubuntu 20.04 LTS.
4. **SSH Configuration**: SSH client configuration must be set up to use private keys and refuse password authentication.

### SSH Installation Guide

1. Ensure SSH is installed:
   ```bash
   $ sudo apt-get install openssh-client
   ```

2. Verify the installation:
   ```bash
   $ ssh -V
   ```

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. Use a private key**      | Write a Bash script to connect to a server using a private key | `0-use_a_private_key` |
| **1. Create an SSH key pair** | Write a Bash script to create an RSA key pair with a passphrase | `1-create_ssh_key_pair` |
| **2. Client configuration file** | Configure the SSH client to use a private key and refuse password authentication | `2-ssh_config` |
| **3. Let me in!**             | Add an SSH public key to your server to allow access | `3-let_me_in` |
| **4. Client configuration file (w/ Puppet)** | Use Puppet to configure the SSH client to use a private key and refuse password authentication | `100-puppet_ssh_config.pp` |

## Learning Objectives

By completing this project, you will:

- Understand the basics of SSH and its configuration.
- Learn how to create and manage SSH key pairs.
- Gain experience with SSH client configuration.
- Automate SSH configuration tasks using Puppet.

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x0B-ssh`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School in collaboration with the ALX Software Engineering Program to provide hands-on learning in a professional environment.
