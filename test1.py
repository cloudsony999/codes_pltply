import pandas as pd
import plotly.express as px

df=pd.read_csv('dataset/iris.csv')

print(df)
print(df.columns)

plot=px.scatter(
  data_frame=df,
  x='sepal_length',
  y='petal_length',
  title='Plot of Sepal length and Petal length'
  )

plot.show()