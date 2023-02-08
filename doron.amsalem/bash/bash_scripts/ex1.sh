#!/bin/bash
a=`date %Y-%m-%d`
echo $a
for file in *
do 

mv $file $a+$file
done

