import streamlit as st
import pandas as pd
import numpy as np

print('test')

number = st.number_input('Insert sqft_living on a flat or house')

test = 277.88028773 * number - 38891.11523714

st.write('using simple linear regrssion we estimate the price to be:', test)

