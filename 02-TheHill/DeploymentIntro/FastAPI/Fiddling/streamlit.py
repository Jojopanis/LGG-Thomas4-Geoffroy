import streamlit as st
import json
import requests

st.title("Basic calculator test")

options = st.selectbox('Choose an operation',
                    ('Addition','Difference','Multiplication','Division'))
st.write('')
st.write('Select numbers below :')
x = st.slider('X', 0, 100, 10)
y = st.slider('Y', 0, 100, 10)

inputs = {'operation': options, 'x': x, 'y': y}

if st.button('Calculate'):
    res = requests.post(url='http://127.0.0.1:8000/calculate', data=json.dumps(inputs))
    st.subheader(f'Response from the API: {res.text}')