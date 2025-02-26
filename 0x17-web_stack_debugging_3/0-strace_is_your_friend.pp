# Fixes Apache 500 error in WordPress by correcting a PHP file extension typo

{ 'fix-wordpress':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin/:/bin/',
}
