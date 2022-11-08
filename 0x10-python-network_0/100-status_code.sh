#!/bin/bash
#print status code of http request
curl -Ls -o /dev/null -w "%{http_code}" "$1"
