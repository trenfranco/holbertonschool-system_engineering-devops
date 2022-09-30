# Added more traffic limit to Nginx server

# Increasing the ULIMIT
exec { 'ulimitFix':
  command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}
# Restart Nginx
exec { 'nginxRestart':
  command => '/usr/sbin/service nginx restart',
}
