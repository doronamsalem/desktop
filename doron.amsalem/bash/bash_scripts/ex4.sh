echo "please insert directory name:"
read DIR
dirPath=$(find ~ -type d -name $DIR)
echo "please insert limit of bytes:"
read X
for file in $dirPath/*
do
	filesize=$(wc -c $file | awk '{print $1}')
	if [ $filesize -gt $X ]
	then
		rm $file
	fi
done

