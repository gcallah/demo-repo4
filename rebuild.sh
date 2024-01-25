#!/bin/bash
# This runs on PythonAnywhere servers: fetches new code,
# installs needed packages, and restarts the server.

touch rebuild
echo "Rebuilding $PA_DOMAIN"

echo "Pulling code from master"
git pull origin master

echo "Activate the virtual env $VENV for user $PA_USER"
source /home/$PA_USER/.virtualenvs/$VENV/bin/activate

echo "Install packages"
pip install --upgrade -r requirements.txt

echo "Going to reboot the webserver using $API_TOKEN"
pa_reload_webapp.py $PA_DOMAIN

touch reboot
echo "Finished rebuild."
