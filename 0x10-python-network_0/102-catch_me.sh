#!/bin/bash
#make request to 0.0.0.0:5000/catch_me
curl -XPUT -Ls -d user_id=98 0.0.0.0:5000/catch_me
