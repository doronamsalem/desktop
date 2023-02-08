#!/bin/bash
absolute_sum=0
echo "insert numbers for calculate there absolute sum:"
read numbers

for num in $numbers
do
	if [ $num -gt 0 ]
	then
		absolut_sum=$(( $absolut_sum+$num ))
	else
		absolut_sum=$(( $absolut_sum - $num ))
	fi
done
echo $absolut_sum
