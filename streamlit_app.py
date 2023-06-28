import streamlit as st
import pandas as pd
from IPython.display import IFrame

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('WO Analysis')

st.sidebar.subheader('Client Info')
time_hist_color = st.sidebar.selectbox('Client Name', ('Shell', 'MCHS' , 'MSFT')) 

st.sidebar.subheader('Time Period')

st.markdown('### Dashboard')
col = st.columns(1)
col.metric(MCHS = IFrame(src = "https://app.powerbi.com/reportEmbed?reportId=d536c4e0-6fdc-4b4b-94b0-5674ad8c5527&autoAuth=true&ctid=0159e9d0-09a0-4edf-96ba-a3deea363c28", width = 1140, height = 541.25))
