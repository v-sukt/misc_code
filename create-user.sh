#!/bin/bash
#the script adds the specified ssh user in the specified arg-1 with the server name/ip provided as arg2
#arg2 server name(as refence in /etc/hosts)/ip
#arg3 is the key-name  where key.name is private key and key-name.pub is publik ey

[ $# -lt 3 ] && echo -e "Usage:\t $0 {username} {target-server} {public-key-path}" && exit 1
#check if the server is accessible
#test : run the ls command remotely
ssh ubuntu@${2} ls>/dev/null; [ $? -ne 0 ] && echo "no acess to server : ${2} with user `whoami`" && exit 2
#if result is not failure proceed

#check if user exists
ssh ubuntu@${2} id -u ${1}>/dev/null; [ $? -eq 0 ] && echo "the user ${1} already exists on ${2}" && exit 3

#copy the key-name.pub file to /tmp folder on server
scp $3 ubuntu@${2}:/tmp/userkey.pub; [ $? -ne 0 ] && echo "cant write to server : ${2}" && exit 4

#login to the server and heretag
ssh ubuntu@${2}<<-HERETAG
  sudo -s
  useradd -m -d /home/${1} -s "`which bash`" ${1}
  mkdir ~${1}/.ssh
  cat /tmp/userkey.pub >>~${1}/.ssh/authorized_keys
  rm -f /tmp/userkey.pub
  chown $1.$1 -R ~${1}/.ssh
  id ${1}
  echo "check if all izz well in by logging in from terminal"
  exit
HERETAG

echo "Done..!"
