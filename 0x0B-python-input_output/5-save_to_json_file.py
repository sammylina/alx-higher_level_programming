#!/usr/bin/python3
"""JSON file module"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file

    Args:
        my_obj (obj): JSON object to be written
        filename (str): text file to save the JSON string

    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
