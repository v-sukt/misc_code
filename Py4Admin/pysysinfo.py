#!/usr/bin/env python
#A System Information gathering script
import subprocess

#Command 1
uname = "uname"
uname_arg = "-a"
print "Gathering system information using %s command: \n" % uname
subprocess.call([uname, uname_arg])

#Command 2
diskspace = "df"
diskspace_arg = "-h"
print "Gathering the diskspace information using %s command: \n" % diskspace
subprocess.call([diskspace, diskspace_arg])
