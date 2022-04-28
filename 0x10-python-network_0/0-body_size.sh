#!/bin/bash
# print content-length of a remote resource
curl -Is "$1" | grep -i content-length | awk '{print $2}'
