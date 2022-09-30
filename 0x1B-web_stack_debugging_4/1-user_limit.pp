# now the holberton user can login and open files with no error code

# more hard file limit to holb user
exec { 'hardFileLimitAdded':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# more soft file limit to holb user
exec { 'softFileLimitAdded':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
