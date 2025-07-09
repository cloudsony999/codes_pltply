import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
st.markdown('GAPMINDER DASHBOARD')
df=pd.read_csv('gapminder_data_graphs.csv')
st.dataframe(df)
unique_years=df['year'].unique()
print(unique_years)


selected_year=st.selectbox(label='Year',options=unique_years)
dfplot=df[df['year']==selected_year]
st.write(dfplot)

average_gdp=round(dfplot['gdp'].mean(),2)
average_life_exp=round(dfplot['life_exp'].mean(),2)
average_hdi=round(dfplot['hdi_index'].mean(),2)

col1,col2,col3=st.columns([1,1,1])
col1.metric(label='Average GDP',value=average_gdp)
col2.metric(label='Average Life Expentency',value=average_life_exp)
col3.metric(label='Average HDI',value=average_hdi)


title='PLOT OF GDP VS LIFE EXPECTENCY for Year {}'.format(selected_year)
scatter_plot=px.scatter(
    data_frame=dfplot,
    x='gdp',
    y='life_exp',
    color='continent',
    title=title)

st.plotly_chart(scatter_plot)

