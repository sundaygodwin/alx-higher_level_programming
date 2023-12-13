#!/usr/bin/python3
# 6-from_json_string.py
"""program defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object that represents a JSON string."""
    
    return json.loads(my_str)
