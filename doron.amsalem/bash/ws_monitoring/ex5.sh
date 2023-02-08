#!/bin/bash

if [[ $? == 0 ]]
then
        logger "successful run"
else [[ $? == 1 ]]
	eho failed

