
import numpy as np, os
from bertopic import BERTopic
from pprint import pprint
from typing import Iterable, Tuple

# global variables
doc_path = '../CUAD_v1/full_contract_txt/'
topic_model = BERTopic()

def find_topics(documents: Iterable[str], search_term: str, top_n: int = 5):
    """
    Wrapper for BERTopic.find_topics function.

    Parameters:
        documents (Iterable[str]): Document content as iterable of strings to fir BERTopic.
        search_term (str): The term you want to use to search for topics.
        top_n (int): The number of topics to return.

    Returns:
        Tuple
    """
    topic_model.fit(documents=documents)
    return topic_model.find_topics(search_term=search_term, top_n=top_n)

if __name__ == '__main__':
    documents = np.asarray(a=list([open(file=doc_path + filename, mode='r').read() for filename in os.listdir(path=doc_path)]))
    topics = find_topics(documents=documents, search_term='agreement')
    pprint(topics)
    pprint(topic_model.get_topic(0))
