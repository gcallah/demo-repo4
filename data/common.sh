#!/bin/sh
# Some common shell stuff.

echo "Importing from common.sh"

DB=gamesDB
USER=gcallah
CONNECT_STR="mongodb+srv://koukoumongo1.yud9b.mongodb.net/"
if [ -z $DATA_DIR ]
then
    DATA_DIR=/Users/gcallah/Classes/demo-repo4/data
fi
BKUP_DIR=$DATA_DIR/bkup
EXP=/usr/local/bin/mongoexport
IMP=/usr/local/bin/mongoimport

if [ -z $MONGO_PASSWD ]
then
    echo "You must set MONGO_PASSWD in your env before running this script."
    exit 1
fi

declare -a GameCollections=("games" "users")
