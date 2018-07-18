#!/usr/bin/env bash
#A sample function

function shfunc(){
    printf "Hello World\n"
}

for (( i=0; i<5; i++)); do
    shfunc
done
