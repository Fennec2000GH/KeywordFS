
from genericpath import exists, isfile
import json, os
from pprint import pprint
from keyword_extraction import *
from topic_modeling import *
# from xml_parser import *

def file_to_json(path: str, storage_path: str = 'storage'):
    """
    Converts file containing text to stored JSON object to track topics and keywords.

    Parameters:
        path (str): Path to file to be converted to JSON object.
        storage_path (str): Path to directory to store JSON object.

    Returns:
        None
    """
    # edge case
    if not (os.path.exists(path=path) and os.path.isfile(path=path)):
        raise ValueError(f'{path} is not a valid path to a file.')

    os.makedirs(path=storage_path, exist_ok=True)    
    with open(file=path, mode='r') as file:
        json_dict = dict({
            'keywords': set(),
            'topics': set(find_topics(documents=))
        })
        json.dump(obj=file)
