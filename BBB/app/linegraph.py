import plotly
import plotly.graph_objs as go
from app import db, app
from app.models import City, Weather
import pandas as pd
import numpy as np
import json

def create_plot(cityName):

    city = City.query.filter_by(name=cityName).first_or_404()

    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Line(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
