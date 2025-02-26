# Fixes Apache 500 error in WordPress by correcting a PHP file extension typo

{ 'fix-wordpress':
  command => 'sed -i "s|wp-setting.php|wp-settings.php|g" /var/www/html/wp-config.php',
  path    => '/usr/bin:/bin',
  onlyif  => 'grep -q "wp-setting.php" /var/www/html/wp-config.php',
}
