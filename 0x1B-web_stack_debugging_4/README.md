# 0x1B. Web Stack Debugging #4

## Background Context
In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure. Using ApacheBench, we simulate HTTP requests to the server and identify performance issues. The goal is to fix the stack so that it handles high traffic without failing requests.

## General

| Category | Details |
|----------|---------|
| **Environment** | Ubuntu 14.04 LTS |
| **File Structure** | All files should end with a new line |
| **README** | A `README.md` file at the root of the project folder is mandatory |
| **Puppet Manifests** | Must pass `puppet-lint` version 2.1.1 without errors |
| **Puppet Version** | Files will be checked with Puppet v3.4 |

## More Info

### Puppet Installation
To install `puppet-lint`, run the following commands:
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Tasks

| Task | Description | Files |
|------|-------------|-------|
| **0. Sky is the limit, let's bring that limit higher** | Fix the Nginx web server to handle 2000 requests with 100 concurrent connections without failing. | `0-the_sky_is_the_limit_not.pp` |
| **1. User limit** | Change the OS configuration to allow the `holberton` user to log in and open files without errors. | `1-user_limit.pp` |

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x1B-web_stack_debugging_4`

## Mission Director

This project is part of the ALX Software Engineering Program.

## Developer

**Codename**: Achraf Sadeq

## Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.

