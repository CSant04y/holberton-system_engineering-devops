# This script creats a file and specifies the owner, group-owner and file permissions
file { '/tmp/holberton':
    ensure  => file,
    owner   => www-data,
    group   => www-data,
    mode    => '0744',
    content => 'I love Puppet',
}
