import streamlit as st
from PIL import Image
import numpy as np

st.title("FX CURRENCY CONVERTER")

currency = ['NGN', 'USD', 'JPY', 'CAD', 'GBP']

conv = [1, 0.00065, 0.10, 0.0008, 0.00051]

def curr_converter(amt,cur_f,cur_t):

    ind_f = currency.index(cur_f)
    ind_t = currency.index(cur_t)

    rate_f = conv[ind_f]
    rate_t = conv[ind_t]

    value = amt * (rate_t/rate_f)
    value = round(value,2)
    return value

amt = st.number_input("Amount")
cur_f = st.selectbox("from",currency)
cur_t = st.selectbox("to",currency)

if st.button("convert"):
    val = curr_converter(amt,cur_f,cur_t)
    st.success(val)