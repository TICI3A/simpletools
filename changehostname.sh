#!/bin/bash

# **********************
# changehostname
# 
#
# v.2021.03.12 ubuntu 20.04 test
# ***********************

function main
{
    oldhost=$HOSTNAME
    newhost=$1
    echo "actual hostname $oldhost"
    sudo hostnamectl set-hostname $newhost
    sudo sed -i "s/${oldhost}/${newhost}/" /etc/hosts
    hostnamectl
    echo "system go to reboot in 5 seg"
    sleep 5
    sudo reboot
}


if [ "$#" -lt 1 ]
then
  echo "Usage: "
  echo "      $0 newhostname"
  exit 85
else
  main $1
fi

exit 0