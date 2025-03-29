import json
from pathlib import Path
from collections import OrderedDict

def read_json(fname):
    """
    Read a JSON file and return its contents as a dictionary.
    
    Args:
        fname (str or Path): The path to the JSON file.
        
    Returns:
        dict: The contents of the JSON file as a dictionary.
    """
    fname = Path(fname)
    with open(fname, 'r') as handle:
        return json.load(handle, object_hook=OrderedDict)
    
def write_json(data, fname):
    """
    Write a dictionary to a JSON file.
    
    Args:
        data (dict): The dictionary to write to the JSON file.
        fname (str or Path): The path to the JSON file.
    """
    fname = Path(fname)
    with open(fname, 'wt') as handle:
        json.dump(data, handle, indent=4, sort_keys=False, ensure_ascii=False)