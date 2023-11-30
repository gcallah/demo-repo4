#!/bin/sh
# Script to backup production database to JSON files.

. ./common.sh

for collection in ${GameCollections[@]}; do
    echo "Backing up $collection"
    $EXP --collection=$collection --db=$DB --out=$BKUP_DIR/$collection.json $CONNECT_STR --username $USER --password $MONGO_PASSWD
done

git add $BKUP_DIR/*.json
git add $BKUP_DIR/*.json
git commit $BKUP_DIR/*.json -m "Mongo DB backup"
git pull origin master
git push origin master
