# Configs a file to access the server without password
# using puppet
file { '/home/tnkm_a/.ssh':
  ensure => 'directory',
  mode   => '0700',
  owner  => 'tnkm_a',
}

file { '/home/tnkm_a/.ssh/config':
  ensure  => 'file',
  content => "
Host web-01
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
  mode    => '0600',
  owner   => 'tnkm_a',
}
