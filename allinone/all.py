import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Visualization app")

st.sidebar.subheader("Visualization Settings")

uploaded_file=st.sidebar.file_uploader(
  label='Upload your CSV/Excel here!!!',
  type=['csv','xlsx']
)
print(uploaded_file)

global df
global neumeric_columns
global non_neumeric_columns
if uploaded_file is not None:
  try:
    df=pd.read_csv(uploaded_file)
  except Exception as e:
    print(e)
    df=pd.read_excel(uploaded_file)

  dis=st.sidebar.checkbox(label='Would U like to see the dataset?')

  if dis:
    st.write(df)

  #extract neumeric columns
  neumeric_columns=list(df.select_dtypes(['float','int']))

#extract non-neumeric columns
  non_neumeric_columns=list(df.select_dtypes(['object']))
  non_neumeric_columns.append('None')


  st.write(neumeric_columns)
  st.write(non_neumeric_columns)

  # Add a select wizard

  chart_select=st.sidebar.selectbox(
    label='Select the Visualization type',
    options=['ScatterPlot','LinePlot','Histogram']
  )


  try:
    if chart_select=='ScatterPlot':
      st.sidebar.subheader('Settings for ScatterPlot')
      x_value=st.sidebar.selectbox(label='X axis',options=neumeric_columns)
      y_value=st.sidebar.selectbox(label='Y axis',options=neumeric_columns)
      color_value=st.sidebar.selectbox(label='Color',options=non_neumeric_columns)
      plot=px.scatter(
        data_frame=df,
        x=x_value,
        y=y_value,
        color=color_value

      )
      st.plotly_chart(plot)

  

    if chart_select=='Histogram':
      st.sidebar.subheader('Settings for Histogram')
      x=st.sidebar.selectbox(label='Feature',options=neumeric_columns)
      bin_size=st.sidebar.slider(label='Number of Bins',
                                 min_value=10,
                                 max_value=100,
                                 value=50)
      plot=px.histogram(data_frame=df,
                        x=x,
                        nbins=bin_size)
      st.plotly_chart(plot)
    if chart_select=='LinePlot':
      st.sidebar.subheader('Settings for LinePlot')
      x_value=st.sidebar.selectbox(label='X Axis',options=neumeric_columns)
      y_value=st.sidebar.selectbox(label='Y Axis',options=neumeric_columns)
      plot=px.line(data_frame=df,
                   x=x_value,
                   y=y_value)

      
      st.plotly_chart(plot)

  except Exception as e:
    print(e)
      


