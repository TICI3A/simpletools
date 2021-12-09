#!/bin/bash

version=3.5
minversion=3.5.2

wget --no-check-certificate http://cmake.org/files/v$version/cmake-$minversion.tar.gz
tar -zxvf cmake-$minversion.tar.gz
cd cmake-$minversion
./bootstrap --prefix=/usr
make
make install
