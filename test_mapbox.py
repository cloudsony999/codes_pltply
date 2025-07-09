import pandas as pd
import plotly.express as px

df=pd.read_csv('dataset/us-cities-top-1k.csv')

plot=px.scatter_mapbox(
    data_frame=df,
    lat='lat',
    lon='lon',
    size='Population',zoom=5,hover_name='City',
    title='population across different cities',
    mapbox_style='open-street-map'

)
plot.show()

