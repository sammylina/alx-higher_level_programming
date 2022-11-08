#!/bin/bash
#add custom http header to the request
curl -sL -H 'X-School-User-Id: 98' "$1"
