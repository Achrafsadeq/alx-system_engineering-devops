# This Puppet manifest installs and configures Nginx on an Ubuntu server.
# It ensures Nginx is listening on port 80, serves a "Hello World!" page at the root,

class { 'nginx': 
  package_ensure => 'installed',
  service_ensure => 'running',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @("EOM"),
server {
  listen 80;

  location / {
    root /var/www/html;
    index index.html;
  }

  location /redirect_me {
    return 301 http://example.com;
  }
}
| EOM
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
