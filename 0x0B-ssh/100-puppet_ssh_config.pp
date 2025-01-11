# Title: SSH Client Configuration
# Use Puppet to configure the SSH client to use a private key 
# and refuse password authentication.

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^#?[\s]*PasswordAuthentication',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^#?[\s]*IdentityFile',
}
