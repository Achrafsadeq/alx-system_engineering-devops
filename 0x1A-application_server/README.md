# 0x1A. Application Server

## Background Context
Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project, you will add this piece to your infrastructure, plug it into your Nginx, and make it serve your Airbnb clone project.

## General

| Category | Details |
|----------|---------|
| **Environment** | Ubuntu 16.04 LTS |
| **File Structure** | All files should end with a new line |
| **README** | A `README.md` file at the root of the project folder is mandatory |
| **Python Version** | Everything Python-related must be done using `python3` |
| **Bash Scripts** | Must be executable and pass `Shellcheck` without errors |
| **Config Files** | Must have comments explaining their purpose |

## Tasks

| Task | Description | Files |
|------|-------------|-------|
| **0. Set up development with Python** | Set up a development environment for the AirBnB clone v2 - Web framework on `web-01`. | `README.md` |
| **1. Set up production with Gunicorn** | Set up a production environment with Gunicorn on `web-01`, port 5000. | `README.md` |
| **2. Serve a page with Nginx** | Configure Nginx to serve your page from the route `/airbnb-onepage/`. | `2-app_server-nginx_config` |
| **3. Add a route with query parameters** | Configure Nginx to proxy requests to `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance on port 5001. | `3-app_server-nginx_config` |
| **4. Let's do this for your API** | Serve the AirBnB clone v3 - RESTful API on `web-01` using Nginx and Gunicorn. | `4-app_server-nginx_config` |
| **5. Serve your AirBnB clone** | Serve the AirBnB clone - Web dynamic on `web-01` using Nginx and Gunicorn. | `5-app_server-nginx_config` |
| **6. Deploy it!** | Write a systemd script to start your application server on boot. | `gunicorn.service` |
| **7. No service interruption** | Write a Bash script to reload Gunicorn gracefully without downtime. | `4-reload_gunicorn_no_downtime` |

## Submission

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x1A-application_server`

## Mission Director

This project is part of the ALX Software Engineering Program.

## Developer

**Codename**: Achraf Sadeq

## Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.
