#!/bin/bash
if [[ $? == 0 ]]
then
	logger "successful run"
else
	logger "FAILED"
fi
