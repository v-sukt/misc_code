#!/bin/bash
#A system information gathering script

#Command 1
UNAME="uname -a"
printf "Gathering the system info using $UNAME command: \n"
$UNAME

#Command 2
DISKSPACE="df -h"
printf "Gathering the diskspace info using $DISKSPACE command: \n"
$DISKSPACE
