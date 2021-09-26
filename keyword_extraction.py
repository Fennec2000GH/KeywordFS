import numpy as np, os
from keybert import KeyBERT
from pprint import pprint
from typing import Iterable, Tuple, Union

# global variables
doc_path = '../CUAD_v1/full_contract_txt/'
kw_model = KeyBERT()

def extract_keywords(docs: Union[str, Iterable[str]]):
    """
    Extract keywords from text.

    Parameters:
        text (str): Text to extract keywords from.

    Returns:
        Union[List[Tuple[str, float]], List[List[Tuple[str, float]]]]: The top n keywords for a document with their respective distances to the input document.
    """
    keywords = kw_model.extract_keywords(docs=docs)
    return keywords

if __name__ == '__main__':
    docs = list([open(file=doc_path + filename, mode='r').read() for filename in os.listdir(path=doc_path)])
    kws = extract_keywords(docs=docs)
    pprint(kws)
    pprint(type(kws))
