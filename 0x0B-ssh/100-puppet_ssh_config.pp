# Using Puppet script to create ssh
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',  # or the path to your SSH config file
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',  # or the path to your SSH config file
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}
