import csv
from app import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), index=True, unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    weatherData = db.relationship('Weather', backref='city', lazy=True)

    def __repr__(self):
        return self.name

    def weatherHistory(self):
        weather = Weather.query.filter_by(city_id=self.id)
        return weather

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    date = db.Column(db.DateTime)
    loTemp = db.Column(db.Float)
    hiTemp = db.Column(db.Float)
    avgTemp = db.Column(db.Float)
    gust = db.Column(db.Float)
    precip = db.Column(db.Float)

    def __repr__(self):
        weatherString = '<Weather in {} on {}>'
        return weatherString.format(City.query.get(self.city_id).name, self.date.strftime('%Y-%m-%d'))

class GlobalData(db.Model):
   year = db.Column(db.Integer, primary_key=True)
   temp = db.Column(db.Float)
   precip = db.Column(db.Float)
   seaLevel = db.Column(db.Float)
   storms = db.Column(db.Float)

   def __repr__(self):
      annual = '<{} global average temp: {}, precip: {}, sea level: {}, storms:{}'
      return annual.format(self.year, self.temp, self.precip, self.seaLevel, self.storms)
