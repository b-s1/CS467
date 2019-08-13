from app import db, app
from app.models import City, Weather

def calc_avgs(cityName):

    city = City.query.filter_by(name=cityName).first_or_404()

    data = city.weatherHistory()

    sums = {}

    for day in data:
        year = day.date.year
        if year not in sums:
            if day.avgTemp is not None:
                sums[year] = [day.avgTemp, 1]
            elif day.loTemp is not None and day.hiTemp is not None:
                sums[year] = [(day.loTemp + Day.hiTemp) / 2 , 1]
        else:
            if day.avgTemp is not None:
                sums[year][0] += day.avgTemp
                sums[year][1] += 1
            elif day.loTemp is not None and day.hiTemp is not None:
                sums[year][0] += (day.loTemp + Day.hiTemp) / 2
                sums[year][1] += 1


    avgs = []
    for year in sums:
        avgs.append((year, sums[year][0] / sums[year][1]))

    return avgs
