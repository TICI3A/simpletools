#!/bin/bash

# **********************
# automaticcopy
# 
# v.2021.06.14 fix: se llenaba el disco de copias
# v.2021.05.03 ubuntu 20.04 test
# v.2021.05.11 rsync tested, somes fixs
# ***********************

function main
{
    mkdir -p /storage/sync
    cd /storage
    rsync -lrpg --delete "$1" /storage
    last=$(ls /storage/sync | grep ".*.tar.gz" | tail -1 | awk -F\. '{ print $2 }')
    echo "1 $last"
    if [[ $last -gt 5  ]]
    then
        last=0
    elif [[ $last == ''  ]]
    then
        last=0
    else
        echo "2 $last"
        last=$(($last + 1))
    fi
    
    filename="$1"."$last".tar.gz
    tar -czf "$filename" "/storage/$1"
    mv "$filename" "/storage/sync"
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
