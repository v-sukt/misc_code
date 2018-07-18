#!/usr/bin/env python
#A System Information gathering script
import subprocess

def sysinfo():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information using %s command: \n" % uname
    subprocess.call([uname, uname_arg])

def diskinfo():
    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering the diskspace information using %s command: \n" % diskspace
    subprocess.call([diskspace, diskspace_arg])

def main():
    sysinfo()
    diskinfo()

main()
