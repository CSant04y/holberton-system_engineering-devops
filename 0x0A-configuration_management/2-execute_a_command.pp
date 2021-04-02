# added a procces that is called kill me now
exec {'pkill':
  command => '/usr/bin/pkill killmenow'
}
