#!/bin/bash
#send data from file using post request
curl -Ls -XPOST -H 'Content-Type: application/json' -d "@$2" "$1"
