#!/usr/bin/python3
"""JSON decoder module"""
import json


def load_from_json_file(filename):
    """read JSON string from a file and return JSON object

    Args:
        filename (str): file that has JSON string

    """
    with open(filename, encoding='utf-8') as file:
        data = file.read()
        return json.loads(data)
