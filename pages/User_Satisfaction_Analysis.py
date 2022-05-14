import streamlit as st

def app():
    st.header("satisfaction")
    df = pd.read_csv('tellco_data.csv', index_col=0)
    df = df.astype(str)