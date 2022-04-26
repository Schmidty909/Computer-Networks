#!/usr/bin/env bash

# tell python not to create ANY cache
export PYTHONDONTWRITEBYTECODE=1

# This is a bash cheat for get the directory of this file.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR/..

DIR=$PWD

# This is here for convenience sake.  Kill any previously run instances
source /home/Admiral/Desktop/Computer-Networks/kill_processes.sh

# Run the processes!
python3 -B $DIR/Computer-Networks/server.py

# Waits for all processes to return or die
wait
