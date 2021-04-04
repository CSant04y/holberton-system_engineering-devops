# Changes config file to turn off password authentication. and use private key intead
file { '/etc/ssh/ssh_config':
  content => 'PasswordAuthentication no
  IdentityFile ~/.ssh/holberton',
}
