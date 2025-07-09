import pandas as pd
import plotly.express as px

df=pd.read_csv('dataset/iris.csv')

print(df)
print(df.columns)

plot=px.scatter(
  data_frame=df,
  size='sepal_width',template='plotly_dark',
  x='sepal_length',
  color='species',
  facet_col='species',
  y='petal_length',
  title='Plot of Sepal length and Petal length'
  )

plot.show()