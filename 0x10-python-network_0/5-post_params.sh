#!/bin/bash
#send post request with data using curl
curl -Ls "$1" -d 'email=test@gmail.com&subject=I will always be here for PLD'
