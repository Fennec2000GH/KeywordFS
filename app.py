
import numpy as np, pandas as pd, pickle, streamlit as st
from pprint import pprint
from keyword_extraction import *
# from topic_modeling import *


# from functions import *

# Aesthetics
st.set_page_config(
    page_title='KeywordFS',
    page_icon='📒',
    layout='centered',
    initial_sidebar_state='expanded'
)

st.image(image='logo.gif')
st.title(body='KeywordFS')

badges = list(['![language](https://img.shields.io/badge/language-python-yellow?style=plastic&logo=appveyor)',
'![backend](https://img.shields.io/badge/backend-KeyBERT-seagreen)',
'[![Star](https://img.shields.io/github/stars/Fennec2000GH/IntelliVision.svg?logo=github&style=social)](https://gitHub.com/Fennec2000GH/IntelliVision)'])

st.write((' ' * 5).join(badges))

# Upload new files
st.markdown(body='## Upload Files')
files = st.file_uploader(
    label='',
    accept_multiple_files=True
)

docs = list([file.read() for file in files])
if st.button(label='Keywords'):
    kws = extract_keywords(docs=docs)
    pprint(kws)
    kws_formatted = np.asarray(a=list([np.asarray(a=list([tup[0] for tup in doc_kws])) for doc_kws in kws]))
    pprint(kws_formatted)

    # global kws_df
    kws_df = pd.DataFrame(
        data=kws_formatted,
        index=np.asarray(list([str(file.name) for file in files])),
        columns=np.arange(1, 6)
    ).astype(dtype=str, copy=True)

    pprint(kws_df)
    kws_df.to_pickle(path='kws_df.pkl')
    st.write(kws_df)
    st.balloons()

# Search for files
st.markdown(body='## Keyword-based Search:')
search_bar = st.text_input(label='')
if st.button(label='🔍'):
    kws_df = pickle.load(file=open(file='kws_df.pkl', mode='rb'))
    match_index = kws_df.isin(values=str(search_bar).split()).any(axis=1)
    st.write(kws_df.index[match_index])
    st.balloons()