#!/usr/bin/python3
"""String to JSON module"""
import json


def from_json_string(my_str):
    """decode a string to JSON object

    Args:
        my_str (str): a string

    """
    return json.loads(my_str)
