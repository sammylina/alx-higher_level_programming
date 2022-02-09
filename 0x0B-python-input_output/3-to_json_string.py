#!/usr/bin/python3
"""Json module"""
import json


def to_json_string(my_obj):
    """serialize a JSON object to string

    Args:
        my_obj (obj): JSON object

    """
    return json.dumps(my_obj)
