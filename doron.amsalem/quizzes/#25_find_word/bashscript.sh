#!/bin/bash
        echo "insert word:"
        read word
	echo "insert path:"
        read path

	grep -rnw $path -e $word
