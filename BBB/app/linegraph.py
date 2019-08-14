import plotly
import plotly.graph_objs as go
from app import db, app
from app.models import City, Weather
import pandas as pd
import numpy as np
import json


#takes a list of tuples (year, average) and returns a json dump of the graph data
def create_plot(avgs, title, color):


    x = [] 
    y = []
    for year in avgs:
        x.append(year[0])
        y.append(year[1])
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Scatter(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y'],
            marker=dict(color=color)
        )
    ]
    
    layout = dict(title=title)
    fig = dict(data=data, layout=layout)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
