#!/bin/bash

version=1.1.1k

wget https://www.openssl.org/source/openssl-$version.tar.gz
tar -zxvf openssl-$version.tar.gz
cd openssl-$version
./config --prefix=/usr/local/openssl
make
make install

ln -s /usr/local/openssl/include/openssl /usr/include/openssl
ln -s /usr/local/openssl/lib/libssl.so.1.1 /usr/local/lib64/libssl.so
ln -s /usr/local/openssl/bin/openssl /usr/bin/openssl

echo "/usr/local/openssl/lib" >> /etc/ld.so.conf 
ldconfig -v > /dev/null

ln -s /usr/local/openssl/lib/libssl.so.1.1 /usr/lib64/libssl.so.1.1
ln -s /usr/local/openssl/lib/libcrypto.so.1.1 /usr/lib64/libcrypto.so.1.1