# 0x17. Web Stack Debugging #3
## Background Context
When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something students can do!

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites... It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

## Requirements

### General
| Category | Details |
|----------|---------|
| **Environment** | Ubuntu 14.04 LTS |
| **File Structure** | All files should end with a new line |
| **README** | A `README.md` file at the root of the project folder is mandatory |
| **Code Style** | Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors |
| **Execution** | Your Puppet manifests must run without error |
| **Documentation** | Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about |
| **File Extension** | Your Puppet manifests files must end with the extension `.pp` |
| **Puppet Version** | Files will be checked with Puppet v3.4 |

## More Info

### Install `puppet-lint`
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Tasks

| Task | Description | Files |
|------|-------------|-------|
| **0. Strace is your friend** | Using `strace`, find out why Apache is returning a 500 error. Fix it and automate the fix using Puppet. | `0-strace_is_your_friend.pp` |

### Task 0: Strace is your friend
Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

**Hint:**
- `strace` can attach to a current running process
- You can use tmux to run strace in one window and `curl` in another one

**Requirements:**
- Your `0-strace_is_your_friend.pp` file must contain Puppet code
- You can use whatever Puppet resource type you want for your fix

**Example:**
```
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep ALX
<title>ALX &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="ALX &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="ALX &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="ALX" /></div>    </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">ALX</a></h1>
        <p>Yet another bug by a ALX student</p>
root@e514b399d69d:~#
```

## Submission
- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Achrafsadeq/alx-system_engineering-devops)
- **Directory**: `0x17-web_stack_debugging_3`
- **File**: `0-strace_is_your_friend.pp`

## Mission Director

This project is part of the ALX Software Engineering Program.

## Developer

**Codename**: Achraf Sadeq

## Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.
