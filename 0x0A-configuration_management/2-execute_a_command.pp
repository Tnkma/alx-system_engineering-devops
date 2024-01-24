# Kills a process called killmwnow using puppet
exec { 'killmenow_process':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
