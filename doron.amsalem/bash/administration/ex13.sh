#!/bin/bash

echo "enter service name"
read service

echo $service "is" `systemctl is-active $service`

PS3="Enter a number: "
select operation in start stop leave
do
	if [[ $operation == leave ]]
	then 
		exit
	else
		systemctl $operation $service
	fi	
done
