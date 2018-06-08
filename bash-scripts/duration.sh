#!/bin/bash

#
# Conversion of date from epoch 
# function accepts epoch value difference (seconds) as argument 
#

function duration(){
    #convert the secs to meaningful duration term - format as variable declared TIMEFMT, can be overriden with --format argument
    # format can take values in the case statement
    
    # here the function returns value 0 if duration is more than 1 year, is negative or is blank
    [ -z $1 ] || [ ${1} -lt 0 -o ${1} -ge 31556926 ] && printf "%03d:%02d:%02d\n" && return 1 || my_seconds=$1
    
    # if --format argument is passed with format string, override the format string
    [ "$#" -eq 3 -a "${2}" == "--format" ] && shift 2 && TIMEFMT=${1} 

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

    #print to needed format default format if not set is YMWD,HH:MM:SS
    # further enhancement - at runtime decide whih term will keep the highest value 
    # say for MWD the year will be stored as that many no. of months
    case in ${TIMEFMT:="YMWD,HH:MM:SS"}
        "YMWD,HH:MM:SS" )
            printf "%04dYear(s) %02dMonth(s) %02dWeek(s) %02dDday(s), %02d:%02d:%02d\n" $year $month $week $day $hour $min $sec ;;
        "MWD,HH:MM:SS" )
            printf "%02dMonth(s) %02dWeek(s) %02dDday(s), %02d:%02d:%02d\n" $month $week $day $hour $min $sec ;;
        "WD,HH:MM:SS")
            printf "%02dWeek(s) %02dDay(s), %02d:%02d:%02d\n" $week $day $hour $min $sec ;;
        "D,HH:MM:SS")
            printf "%02dDay(s), %02d:%02d:%02d\n" $day $hour $min $sec ;;
        "HH:MM:SS" )
            printf "%03d:%02d:%02d\n" $hour $min $sec ;;
        * ) # default match Months, weeks days format
            printf "%02dMonth(s) %02dWeek(s) %02dDay(s), %02d:%02d:%02d\n" $month $week $day $hour $min $sec ;;
    esac
}
