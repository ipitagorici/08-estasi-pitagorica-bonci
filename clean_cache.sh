#!/bin/bash

# Finds all the cache folders (media/ and __pycache__/) and
# deletes them. 

CACHE_FOLDERS=("media" "__pycache__")

for TODELETE in ${CACHE_FOLDERS[@]}; do
    for DIR in `find ./ -type d -name $TODELETE`; do 
        rm -rf $DIR
    done
done