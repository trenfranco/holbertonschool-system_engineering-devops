#server config

file_line { 'Identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
file_line { 'disable password':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
