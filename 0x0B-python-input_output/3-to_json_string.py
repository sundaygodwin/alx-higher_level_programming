#!/usr/bin/python3
"""Program defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON  that represents a string object."""
    return json.dumps(my_obj)
