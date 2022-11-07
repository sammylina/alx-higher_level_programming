#!/bin/bash
#send delete request to url(user provided)
curl -XDELETE -L "$1"
