#!/bin/bash

git add *
git status
echo "add commit ya gever:"
read commit
git commit -m "$commit"
git push
