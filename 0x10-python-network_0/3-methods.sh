#!/bin/bash
#print http methods the server supports
curl -ILs -XOPTIONS "$1" | grep -i 'allow' | cut -b 8-
