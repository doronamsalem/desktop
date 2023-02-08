#!/bin/bash
echo please insert path:
read userPa
echo $userPa
echo "in this directory you have "`ls ${userPa} | wc -l` "files" 



#echo "in this directory you have `ls ~/Desktop | wc -l` "files"
