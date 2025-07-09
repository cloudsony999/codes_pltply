import streamlit as st

col1,col2,col3=st.columns(3,gap='large',vertical_alignment='top')

with col1:
    st.header("I AM COLUMN 1")
    st.image('t1.jpg')

with col2:
    st.header("I AM COLUMN 2")
    st.image('t2.jpg')

with col3:
    st.header("I AM COLUMN 3")
    st.image('t3.jpg')