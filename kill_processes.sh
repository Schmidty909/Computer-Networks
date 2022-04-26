#!/usr/bin/env bash

# Kill all currently-running instances of PSS processes.

# This is a bash cheat for get the directory of this file.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR/..

DIR=$PWD

processes="$(pgrep -f -l $DIR)" # get processes running

if [ -n "${processes}" ];       # check if any processes running
then

    for p in $processes;
    do

        if [[ "$p" =~ python* ]];   #check if process name is "python"
        then

            # kill the process using the associated PID
            echo "$previous" | sudo xargs kill

        fi

        previous=$p  # save previous element

    done

    pkill -f -9 server.py
    echo "Previous instances of server killed.";

else
    echo "There are no more previous instances of server to kill.";
fi
