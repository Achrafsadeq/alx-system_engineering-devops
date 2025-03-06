# Change OS configuration to allow Holberton user login and file access without errors  
exec { 'Update OS Limits for Holberton User':
  command => 'sudo sed -i "s/4/40000/" /etc/security/limits.conf; sudo sed -i "s/5/50000/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin'],
  returns => [0, 1]
}
