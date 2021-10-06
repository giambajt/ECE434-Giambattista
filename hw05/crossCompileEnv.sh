#!/bin/sh
#This shell script just takes the file path give and cross compiles it for arm
#The output file will be named a.out
#The commands I used to get to this point are:
#sudo apt-get install libc6-armel-cross libc6-dev-armel-cross binutils-arm-linux-gnueabi libncurses5-dev build-essential bison flex libssl-dev bc
#sudo apt-get install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf
arm-linux-gnueabihf-gcc $1
