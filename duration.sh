#!/bin/bash

#
# Conversion of date from epoch 
# function accepts epoch value difference as argument 
#


function duration(){
    [ -z $1 ] && return 0 || my_seconds=$1
    year=$(($my_seconds/31556926))
    my_seconds=$(($my_seconds%31556926))
    month=$(($my_seconds/2629743))
    my_seconds=$(($my_seconds%2629743))
    week=$(($my_seconds/604800))
    my_seconds=$(($my_seconds%604800))
    day=$(($my_seconds/86400))
    my_seconds=$(($my_seconds%86400))
    hour=$(($my_seconds/3600))
    my_seconds=$(($my_seconds%3600))
    min=$(($my_seconds/60))
    my_seconds=$(($my_seconds%60))
    sec=$my_seconds

    printf "%04dY %02dM %02dW %02dD %02d:%02d:%02d\n" $year $month $week $day $hour $min $sec
}

