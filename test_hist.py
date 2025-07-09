import pandas as pd
import plotly.express as px

df=pd.read_csv('dataset/iris.csv')

plot=px.histogram(
  data_frame=df,
  x='sepal_length',
  nbins=15,
  color='species',
  barmode='group',
  title='distribution of sepal length'
)

plot.show()