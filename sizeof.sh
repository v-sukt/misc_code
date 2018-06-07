#!/bin/bash

#
# Sizeof to convert the size to human readable size - uses unmfmt to get the info
# ... output : echos the human readable value
#     Useful with du -sb - selective file size:
#          size_val=$(du -sb /mnt/files/ --exclude='*pyc' --exclude='*.o' | awk '{ total += $1; }; END { print total }')
#     Usage: sizeof $size_val
#


function sizeof(){
    [ -z $1 ] && my_size=0 || my_size=$1
    echo -n $(numfmt --to=iec-i --suffix=B $my_size)
}
