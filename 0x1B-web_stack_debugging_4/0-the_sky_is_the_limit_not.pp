# to increase amount of trafic

# Increase
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}