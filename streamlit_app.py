import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('WO Analysis')

st.sidebar.subheader('Client Info')
time_hist_color = st.sidebar.selectbox('Client Name', ('Shell', 'MCHS' , 'MSFT')) 

st.sidebar.subheader('Time Period')
