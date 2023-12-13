#!/usr/bin/python3
"""program defines a JSON file-reading function."""

import json


def load_from_json_file(filename):
    """program initialize a Python object from a JSON file."""
    
    with open(filename) as f:
        return json.load(f)
