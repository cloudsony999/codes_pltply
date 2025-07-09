import pandas as pd
import plotly.express as px

df=pd.read_csv('dataset/iris.csv')
'''
plot=px.box(
  data_frame=df,
  x='species',
  y='sepal_width',
  title='Box plot of sepal_width across different specis'
)

'''
plot=px.violin(
  data_frame=df,
  x='species',
  y='sepal_width',
  color='species',box=True,
  title='VIOLIN plot of sepal_width across different specis'
)

plot.show()