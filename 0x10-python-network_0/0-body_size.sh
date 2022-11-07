#!/bin/bash
# print content length of requested url
curl -LIs "$1" | grep -i 'content-length' | cut -d ' ' -f2
