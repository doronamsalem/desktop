#!/bin/bash

echo "please enter name of directory: "
read dir
dirPath=$(find ~ -type d -name $dir)
for item in $dirPath/*
 do 	
 file ${item}
 done

