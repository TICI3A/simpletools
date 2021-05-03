#!/bin/bash

# **********************
# automaticcopy
# 
#
# v.2021.05.03 ubuntu 20.04 test
# ***********************

function main
{
    cd /tmp
    cp "$1" /tmp -r
    tar -czf "$1".tar.gz "/tmp/$1"

}



if [ "$#" -lt 1 ]
then
  echo "Usage: "
  echo "      $0 /absolute/path/to/copy"
  exit 85
else
  main $1
fi

exit 0