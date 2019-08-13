import plotly
import plotly.graph_objs as go
import pandas as pd

import json

import app, db

from app.models import City, Weather

def create_plot(cityName):
    
    city = City.query.filter(City.name == cityName).first_or_404()
    data = Weather.query.filter(Weather.city_id == city.id).all()
    years = []
    for day in data:
        if day.date.year not in years:
            years.append(day.date.year)
    avgs = {}
    for year in years:
        if year not in avgs:
            avgs[year] = [0, 0]
    for day in data:
        if day.avgTemp is not None:
            avgs[day.date.year][0] += day.avgTemp
            avgs[day.date.year][1] += 1
    temps = []
    for year in avgs:
        if avgs[year][1] is None or avgs[year][1] < 180:
            years.remove(year)
        else:
            temps.append(avgs[year][0] / avgs[year][1])


    df = pd.DataFrame({'year': years, 'average temp': temps})


    data = [
        go.Bar(
            x=df['year'],
            y=df['average temp']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
