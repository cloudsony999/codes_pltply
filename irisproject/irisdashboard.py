import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')
df=pd.read_csv('../dataset/iris.csv')
print(df)
unique_species=df['species'].unique()
st.title('Iris Dashboard')
col1,col2=st.columns([1,1])
selected=col1.selectbox(label='Species',label_visibility='collapsed',options=unique_species)

show_hist=col2.checkbox(label='Show Histogram',key='ch',)

#subset of data

dfplot=df[df['species']==selected]
st.write(dfplot)

sl_mean=round(dfplot['sepal_length'].mean(),2)
sw_mean=round(dfplot['sepal_width'].mean(),2)
pl_mean=round(dfplot['petal_length'].mean(),2)
pw_mean=round(dfplot['petal_width'].mean(),2)


#define 4 columns

col1,col2,col3,col4=st.columns([1,1,1,1])
col1.metric(label='Sepal length average',value=sl_mean)
col2.metric(label='Sepal width average',value=sw_mean)
col3.metric(label='Petal length average',value=pl_mean)
col4.metric(label='Petal Width average',value=pw_mean)

#add a scatter plot

color_map={
  'setosa':'gray',
  'versicolor':'gray',
  'verginica':'gray'
}

color_map[selected]='blue'
scatter_data=px.scatter(
  data_frame=df,
  color_discrete_map=color_map,
  x='sepal_length',
  y='petal_width',
  color='species',
  size='petal_length',
  title='Sepal length VS Petal width for {}'.format(selected)
)


st.plotly_chart(scatter_data)

if show_hist:
  col5,col6,col7,col8=st.columns([1,1,1,1])

  hist1=px.histogram(data_frame=dfplot,
                    x='sepal_length',color_discrete_sequence=['blue'],
                    title='Distribution of Sepal Length')

  hist2=px.histogram(data_frame=dfplot,
                    x='sepal_width',color_discrete_sequence=['blue'],
                    title='Distribution of sepal_width')


  hist3=px.histogram(data_frame=dfplot,
                    x='petal_length',color_discrete_sequence=['blue'],
                    title='Distribution of petal Length')


  hist4=px.histogram(data_frame=dfplot,
                    x='petal_width',color_discrete_sequence=['blue'],
                    title='Distribution of petal_width')


  col5.plotly_chart(hist1)
  col6.plotly_chart(hist2)
  col7.plotly_chart(hist3)
  col8.plotly_chart(hist4)


