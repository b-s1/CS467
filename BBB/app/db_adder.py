import csv
from app import db
from app.models import City, Weather
from datetime import datetime

def db_add_weather(cityName, filename):
    city = City(name=cityName)
    db.session.add(city)
    db.session.flush()
    with open('app/city_data/{}'.format(filename)) as csvfile:
        f = csv.DictReader(csvfile)
        for row in f:
            try:
                date = datetime.strptime(row['Date'], '%m/%d/%Y')
            except:
                try:
                    date = datetime.strptime(row['DATE'], '%m/%d/%Y')
                except:
                    date = None
            try:
                loTemp = float(row['TMIN'])
            except:
                loTemp = None
            try:
                hiTemp = float(row['TMAX'])
            except:
                hiTemp = None
            try:
                avgTemp = float(row['TEMP'])
            except:
                try:
                    avgTemp = float(row['TEMP'])
                except:
                    avgTemp = None
            try:
                gust = float(row['Wind Gust'])
            except:
                gust = None
            try:
                precip = float(row['Precipitation'])
            except:
                precip = None
            data = Weather(city_id = city.id,
                    date=date,
                    loTemp=loTemp,
                    hiTemp=hiTemp,
                    avgTemp=avgTemp,
                    gust=gust,
                    precip=precip
                    )
            db.session.add(data)
    db.session.commit()
