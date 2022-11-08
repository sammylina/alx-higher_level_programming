#!/bin/bash
#print status code of http request
curl -LIs "$1" | grep 'HTTP' | cut -d ' ' -f2
