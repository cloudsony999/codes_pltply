import streamlit as st

t1,t2,t3=st.tabs(['TAB 1','TAB 2','TAB 3'])

with t1:
    st.header("I AM TAB 1")

with t2:
    st.header("I AM TAB 2")

with t3:
    st.header("I AM TAB 3")