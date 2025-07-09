import pandas as pd
import plotly.express as px

df=pd.read_csv('dataset/tips.csv')

print(df.columns)
print(df.nunique())

plot=px.pie(
    data_frame=df,
    values='tip',
    names='sex',hole=0.5,
    title='pie chart for male and female....'
)

plot.show()