#! /usr/bin/env bash

if [ $# -lt 2 ] || [ $1 -lt 0 ] || [ $1 -gt 65535 ]
then
   echo -e "\nrun with ./startserver.sh <port number> [&]\n"
   exit 0
fi

gunicorn --bind 0.0.0.0:$1 wsgi:app
