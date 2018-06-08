#!/bin/bash

#To give display for the zenity executed as cronjob
export DISPLAY=:0
#script to be started at 18:30

#Sleep till 1850hrs is reached
while [[ `date +%H%M` -lt 1850 ]]; do
	sleep 30s
done

#show dialogue box for Logging. Auto-close after 5 minutes.
if [ `date +%H%M` -eq 1850 ] ; then
(
	for i in `seq 1 5 300` ; do
			j=`echo "($i/300)*100.00" | bc -l`
			echo $j; sleep 5s
	done
) | zenity --progress --auto-close --no-cancel --percentage=0 --text="Its time!! Log your today's time in next 5 minutes" && \
	echo "Hope It's done !" || echo -e "You Closed me"+'\xE2\x98\xB9'
fi

# Check if the time has reached 18:55 so that next shutdown part can be executed
while [[ `date +%H%M` -lt 1855 ]]; do
	sleep 1m
done
sleep 1m

# Shutdown functionality

if [ `date +%H%M` -le 1856 ] ; then
( # Countdown for 5 minutes
	for i in `seq 0 300` ; do
		j=`echo "($i/300)*100" | bc -l`
		echo $j; sleep 1s
	done
) | zenity --progress --auto-close --percentage=0 --text="System is going down in next 5 minutes. \
     Click cancel to change the timer" && /sbin/shutdown -h -t now && exit || \
     new_time=`zenity --entry --text="Please enter new time(in minutes) for shutdown from now" \
     || zenity --warning --text "Nothing entered.. You are on your own now..!!"`
     unset i; shut_time=`echo $new_time*60|bc -l`
# Check if nothnig is entered as New_time and exit
     [ -z $shut_time ] && echo "blank shut time" && exit 2
                       (
		 	for i in `seq 1 $shut_time`; do
     				echo `echo "($i/$shut_time)*100" | bc -l`
                                sleep 1s
			done
			) | zenity --auto-close --progress --percentage=0 --text="The system will go down in"\ $new_time\ "minutes" && /sbin/shutdown -h -t now || zenity --warning --text="Now you're on your Own..!!"
fi
