# 2-puppet_custom_http_response_header.pp
# Ensure Nginx is installed and running
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Add custom HTTP header to Nginx configuration
file_line { 'add_custom_header':
  path    => '/etc/nginx/nginx.conf',
  line    => "    add_header X-Served-By \$hostname;",
  after   => 'http {',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx if the configuration changes
exec { 'reload_nginx':
  command     => '/usr/sbin/nginx -s reload',
  refreshonly => true,
  subscribe   => File_line['add_custom_header'],
}
