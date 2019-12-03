#!/bin/bash

if [ -f $1 ]
then
 open -a macvim $1 
else
 touch $1
 open -a macvim $1 
fi
