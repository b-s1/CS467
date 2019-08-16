import plotly
import plotly.graph_objs as go
from app import db, app
from app.models import City, Weather
import pandas as pd
import numpy as np
import json


#takes a list of tuples (year, average), graph title, and line color and 
#returns a json dump of the graph data
def create_plot(avgs, title, color):

    x = [] 
    y = []

    #splits list of tuples into x and y coords
    for year in avgs:
        x.append(year[0])
        y.append(year[1])
    df = pd.DataFrame({'x': x, 'y': y}) # creating a dataframe

    # creating a plotly graph object of the coordinates
    data = [
        go.Scatter(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y'],
            marker=dict(color=color)
        )
    ]
    
    #applying finishing touches
    layout = dict(title=title)
    fig = dict(data=data, layout=layout)

    #dumping data to be parsed by JavaScript in the page template
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
