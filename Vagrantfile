# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
 
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = "~> 20210916.0.0" # This sets to specific version so that update should not break our code.
 
  # This is configuring the port on which server will start and same will be mapped for the guest.
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Create shared folder, as it was not creating by default
  config.vm.synced_folder ".", "/vagrant"
 
  # This is how we run the script in vagrant
  config.vm.provision "shell", inline: <<-SHELL
    # Disabling the auto update services
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer
  
    #Update the dependenices and downloads
    sudo apt-get update
    sudo apt-get install -y python3-venv zip # Downloads and install python3 and zip
    touch /home/vagrant/.bash_aliases # Creats .bash_alias file, environment variables will be set to this file.
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
 end