#!/bin/bash

version=5.5.0
old=447

wget --no-check-certificate http://mirrors.kernel.org/gnu/gcc/gcc-$version/gcc-$version.tar.gz
tar -zxvf gcc-$version.tar.gz
cd gcc-$version
./configure
make
make install

mv /usr/bin/gcc /usr/bin/gcc$old
mv /usr/bin/c++ /usr/bin/c++$old
mv /usr/bin/cc /usr/bin/cc$old


ln -s /usr/local/bin/x86_64-unknown-linux-gnu-gcc-$version /usr/bin/gcc
ln -s /usr/local/bin/x86_64-unknown-linux-gnu-c++ /usr/bin/c++
ln -s /usr/local/bin/x86_64-unknown-linux-gnu-gcc /usr/bin/cc
