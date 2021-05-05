#!/bin/bash

# **********************
# automaticcopy
# 
#
# v.2021.05.03 ubuntu 20.04 test
# ***********************

function main
{
    mkdir /storage
    cd /storage
    cp "$1" /storage -r
    last=ls /storage | grep ".*.tar.gz" | tail -1 | awk -F\. '{ print $2 }'

    if [[ $last -gt 5  ]]
    then
        last=0
    elif [[ $last == ''  ]]
    then
        last=0
    else
        last=$(($last + 1))
    fi
    
    tar -czf "$1"."$last".tar.gz "/storage/$1"

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