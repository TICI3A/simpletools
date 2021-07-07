#!/bin/bash

version=3.5
minversion=2.5.2

wget https://cmake.org/files/v$version/cmake-$minversion.tar.gz
tar -zxvf cmake-$minversion.tar.gz
cd cmake-$minversion
./bootstrap --prefix=/usr
make
make install