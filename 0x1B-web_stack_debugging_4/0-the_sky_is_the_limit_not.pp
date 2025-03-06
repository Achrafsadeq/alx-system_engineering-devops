# Script to increase Nginx's ULIMIT from 15 to 4096, allowing it to handle more concurrent requests
exec { 'Fix-for-Nginx':
  command => 'sudo sed -i "s/15/4096/" /etc/default/nginx; sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  returns => [0, 1]
}
