import pandas as pd

import plotly.express as px
import streamlit as st
st.set_page_config(layout='wide')
st.title('Auto MPG Dashboard')

df=pd.read_csv('clean_auto_mpg.csv')
unique_origin=list(df['origin'].unique())
unique_origin.sort()
unique_origin_str=['Origin: '+str(origin) for origin in unique_origin]

print(unique_origin)
print(unique_origin_str)

tab1,tab2,tab3=st.tabs([unique_origin_str[0],
                        unique_origin_str[1],
                        unique_origin_str[2]])
with tab1:
    st.subheader(unique_origin_str[0])
    col1,col2,col3,col4=st.columns([1,1,1,1])
    df_tab=df[df['origin']==unique_origin[0]]
    avg_mpg=round(df_tab['mpg'].mean(),1)
    avg_disp=round(df_tab['displacement'].mean(),1)
    avg_hp=round(df_tab['horsepower'].mean(),1)
    avg_wt=round(df_tab['weight'].mean(),1)
    col1.metric(label='Avg MPG',value=avg_mpg)
    col2.metric(label='Avg Displacement',value=avg_disp)    
    col3.metric(label='Avg HorsePower',value=avg_hp) 
    col4.metric(label='Avg Wight',value=avg_wt)
    col5,col6=st.columns([4,1])
    col5.write('I am 4 time bigger')
    col6.write('i am 1 time bigger')

sc=px.scatter(
    data_frame=df_tab,
    x='weight',
    y='horsepower',
    size='displacement',
    hover_name='car name',
    color='cylinders',
    title='Weight VS HP for cars from {}'.format(unique_origin[0])
)
col5.plotly_chart(sc)

hist=px.histogram(
    data_frame=df_tab,
    x='mpg',
    title='MPG Distribution'
)

col6.plotly_chart(hist)
    
    


with tab2:
    st.subheader(unique_origin_str[1])

with tab3:
    st.subheader(unique_origin_str[2])

