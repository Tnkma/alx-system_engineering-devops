# Installs a flask using the puppet
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.0.2',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  require => [Package['python3-pip'], Exec['install_werkzeug']],
}
