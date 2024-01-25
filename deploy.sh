#!/bin/bash
# This shell script deploys a new version to a server.

PROD_DIRS=DataMixMasterProd
STAGING_DIRS=DataMixMasterStaging
SFA_DIRS=APIMixMaster
SFA_ENV=sfa

if [ -z "$1" ]
then
    echo "Must choose prod, staging, or sfa for deployment target."
    exit 1
else
    TARGET=$1
    if [ "$TARGET" == "prod" ]
    then
        PROJ_DIR=$PROD_DIRS
        VENV=$PROD_DIRS
        PA_DOMAIN="api.datamixmaster.com"
    elif [ "$TARGET" == "sfa" ]
    then
        PROJ_DIR=$SFA_DIRS
        VENV=$SFA_ENV
        PA_DOMAIN="SFAKnowledgeHub.pythonanywhere.com"
    else
        PROJ_DIR=$STAGING_DIRS
        VENV=$STAGING_DIRS
        PA_DOMAIN="athenakoukou.pythonanywhere.com"
    fi
fi
echo "Project dir = $PROJ_DIR"
echo "PA domain = $PA_DOMAIN"
echo "Virtual env = $VENV"

if [ $TARGET == "sfa" ]
then
    if [ -z "$SFA_PWD" ]
    then
        echo "The PythonAnywhere password for SFA (SFA_PWD) must be set in the env."
        exit 1
    else
        PA_PWD=$SFA_PWD
    fi
else
    if [ -z "$PA_PWD" ]
    then
        echo "The PythonAnywhere password var (PA_PWD) must be set in the env."
        exit 1
    fi
fi

if [ -z "$2" ]
then
    PA_USER='athenakoukou'
else
    PA_USER=$2
fi
echo "PA user = $PA_USER"
echo "PA password = $PA_PWD"

echo "SSHing to PythonAnywhere."
sshpass -p $PA_PWD ssh -o "StrictHostKeyChecking no" $PA_USER@ssh.pythonanywhere.com << EOF
    cd ~/$PROJ_DIR; PA_USER=$PA_USER PROJ_DIR=~/$PROJ_DIR VENV=$VENV PA_DOMAIN=$PA_DOMAIN ./rebuild.sh
EOF
