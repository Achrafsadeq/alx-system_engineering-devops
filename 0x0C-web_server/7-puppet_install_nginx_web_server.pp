# Puppet manifest to install and configure Nginx web server
# Includes redirect configuration and Hello World page

# Update package list before installing nginx
exec { 'update system':
        command => '/usr/bin/apt-get update',
}

# Install nginx package, requires system update first
package { 'nginx':
        ensure => 'installed',
        require => Exec['update system']
}

# Create index page with Hello World content
file {'/var/www/html/index.html':
        content => 'Hello World!'
}

# Add permanent redirect for /redirect_me to YouTube
exec {'redirect_me':
        command => 'sed -i "24i\   rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

# Ensure nginx service is running after installation
service {'nginx':
        ensure => running,
        require => Package['nginx']
}
