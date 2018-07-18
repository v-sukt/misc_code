#!/usr/bin/env bash
#A System Information gathering script

function sysinfo(){
    UNAME="uname -a"
    printf "Gathering the system info using $UNAME command: \n"
    $UNAME
}

function diskinfo(){
    DISKSPACE="df -h"
    printf "Gathering the diskspace info using $DISKSPACE command: \n"
    $DISKSPACE   diskspace = "df"
}

function main(){
    sysinfo
    diskinfo
}

main
