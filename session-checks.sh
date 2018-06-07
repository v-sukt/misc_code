#!/bin/bash

TIMEFMT="D,HH:MM:SS"
HOSTIP=`hostname -I`

log_d=/tmp/test-duration
v_file=${log_d}/$(date +%F)/violation-file.log
e_file=${log_d}/exception-pid-file.txt
l_file=${log_d}/$(date +%F)/index.log

# create file if not available
[ ! -d ${log_d}/$(date +%F) ] && mkdir -p ${log_d}/$(date +%F)
[ ! -e ${v_file} ] && touch ${v_file} 
[ ! -e ${e_file} ] && touch ${e_file} 
[ ! -e ${l_file} ] && touch ${l_file} 

function duration(){
    #convert the secs to meaningful duration term - format as variable declared TIMEFMT
    
    # here the function returns value 0 if duration is more than 1 year, is negative or is blank
    [ -z $1 ] || [ ${1} -lt 0 -o ${1} -ge 31556926 ] && printf "%03d:%02d:%02d\n" && return 1 || my_seconds=$1
    
    # if --format argument is passed with format string, override the format string
    [ "$#" -eq 3 -a "${2}" == "--format" ] && shift 2 && TIMEFMT=${1} 

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

    #print to needed format default format if not set is MWD,HH:MM:SS
    case in ${TIMEFMT:="MWD,HH:MM:SS"}
        "WD,HH:MM:SS")
            printf "%02dWeek(s) %02dDay(s), %02d:%02d:%02d\n" $week $day $hour $min $sec ;;
        "D,HH:MM:SS")
            printf "%02dDay(s), %02d:%02d:%02d\n" $day $hour $min $sec ;;
        "HH:MM:SS" )
            printf "%03d:%02d:%02d\n" $hour $min $sec ;;
        * )
            printf "%02dMonth(s) %02dWeek(s) %02dDay(s), %02d:%02d:%02d\n" $month $week $day $hour $min $sec ;;
    esac
}

function check-active-sessions(){

    #    input
    #       :
    #    process
    #        create temp session file
    #        check active sessions
    #            if check-duration for PID
    #                add the line {user, pid, connected server} as above threshold to violation-file
    #            else if session is in exception-list-file
    #                log as skipping due to exception list with command, user, PID, server, duration
    #            else
    #                skip - no logging for below threshold case
    #        check above threshold file for line more than 0
    #            for (unique user list from violation-file)
    #                trigger alert 
    #            done
    #        clean-up temp-file (violation-file), filure file
    #        copy-truncate-log for the day's execution (50days to be kept) - scipt executed daily
    #    Output:
    #        - log with vilation details
    #        - exit status 0 for all ok
    #        - exit status non-zero for failures 
    #            - trigger mail to admin with failure content stored as ( ) 2>failure-content

    tmpfile=`mktemp`

    lsof -i@${HOSTIP}|tail -n +2 > ${tmpfile}
    
    # evaluate each line as column variables (9 columns assumed)
    while read col{1..9}; do

        # extract required variables
        comm=$(cat -A /proc/${col2}/cmdline)
        srv=$(echo ${col9}|cut -f2 -d ">")

        if ${ dur:=$( check-duration ${col2} 86400) }; then
            
            # check if the PID for long duration is exempted form check
            if $( grep -qw ${col2} ${e_file} ); then
                echo -e "Skipping... PID(${col2}, ${col3}\t${comm}\t${srv}\t${dur} )">>${l_file}
            else
                echo -e "${col3}\t${comm}\t${srv}\t${dur}" >> ${v_file}
            fi

        fi
            
    done<${tmpfile}
    
    rm -f ${tmpfile}

    # check for violation-file and trigger alerts
    if [ -s ${v_file} ]; then
        for user in $(cat ${v_file}|cur -f1 -d " "|sort|uniq); do 
            alert ${user} && echo -e "Alert triggered for {user}" \
            || echo -e "Triggering alert failed for {user}" 
        done
    fi

}

    

function check-duration() {

    #    input
    #    process-id, duration-threshold
    #process
    #    difference between two epochs - current and for the stat %X of proc-directory
    #    {
    #        assumption: once created the directory does't change even after executing commands in it
    #    }
    #return 
    #    0 for below limit
    #    N secs duration for above limit

    duration=$(expr $(date +%s) - $(stat -c%X /proc/${1}) )
    
    if [ ${duration} -le $2 ]; then
        return 0
    else
        return ${duration}
    fi
}


function alert(){

    #input
    #    user-name
    #process
    #    list all processes for more duration
    #    command executed for the process /ptoc/id/cmdline or arguments...
    #    Body: {
    #        enviromnet/command | server connected | duration
    #    }
    #output
    #    mail alert with sendmail
    #exception
    #    PID from acceptable file - logged no mail triggered 
    case $1 in
        "user1")
                # some mail body....
                #echo "Hi, you missed closing following sessions"
                #grep user1 ${v_file}
                ;;
        *)
                # inform admin user doesn't exist; following sessions open
    esac
    return 0
}

(
check-active-sessions
) >> ${l_file}