from app import db, app
from app.models import City, Weather

# reads a city's name in and finds all weather for that city in the database
# returns a list of tuples (year, avg) for temperature for that city
def calc_avgs(cityName):

    city = City.query.filter_by(name=cityName).first_or_404()

    data = city.weatherHistory()

    sums = {}

    for day in data:
        try:
            year = day.date.year
        except:
            continue
        if year not in sums:
            if day.avgTemp is not None:
                sums[year] = [day.avgTemp, 1]
            elif day.loTemp is not None and day.hiTemp is not None:
                sums[year] = [(day.loTemp + day.hiTemp) / 2 , 1]
        else:
            if day.avgTemp is not None:
                sums[year][0] += day.avgTemp
                sums[year][1] += 1
            elif day.loTemp is not None and day.hiTemp is not None:
                sums[year][0] += (day.loTemp + day.hiTemp) / 2
                sums[year][1] += 1

    avgs = []
    for year in sums:
        if sums[year][1] > 200:
            avgs.append((year, sums[year][0] / sums[year][1]))

    return avgs
