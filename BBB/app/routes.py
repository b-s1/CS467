import os
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from werkzeug.urls import url_parse, url_unquote
from app import app, db
from app.forms import FileForm
from app.models import City, Weather, GlobalData
from werkzeug import secure_filename
from app.db_adder import db_add_weather
from app.linegraph import create_plot
from app.calc_avgs import calc_avgs

@app.before_request
def before_request():
    g.cities = City.query.all()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home', cities=g.cities)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = FileForm()
    if form.validate_on_submit():
        cityName = form.city_name.data
        if not os.path.exists('app/city_data'):
            os.mkdir('app/city_data')
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('app/city_data/' + filename)
        db_add_weather(cityName, filename)
        return redirect(url_for('upload'))
    return render_template('upload.html', title='Upload', form=form, cities=g.cities)

@app.route('/city/data/<cityName>', methods=['GET', 'POST'])
def city(cityName):
    cityName = url_unquote(cityName)
    city = City.query.filter_by(name=cityName).first_or_404()
    page = request.args.get('page', 1, type=int)
    weather = city.weatherHistory().paginate(
            page, app.config['LINES_PER_PAGE'], False)
    next_url = url_for('city', cityName=cityName, page=weather.next_num) \
            if weather.has_next else None
    prev_url = url_for('city', cityName=cityName, page=weather.prev_num) \
            if weather.has_prev else None
    return render_template('historicalData.html', title='Historical Weather Data for {}'.format(cityName), weather=weather.items, next_url=next_url, prev_url=prev_url, cities=g.cities, graphName=cityName)

@app.route('/global', methods=['GET', 'POST'])
def globalData():
    page = request.args.get('page', 1, type=int)
    weather = GlobalData.query.paginate(
            page, app.config['LINES_PER_PAGE'], False)
    next_url = url_for('globalData', page=weather.next_num) \
            if weather.has_next else None
    prev_url = url_for('globalData', page=weather.prev_num) \
            if weather.has_prev else None
    return render_template('globalData.html', title='Gloabl Context Weather History', weather=weather.items, next_url=next_url, prev_url=prev_url, cities=g.cities)

@app.route('/test/global')
def testGlobal():
   return 0



@app.route('/city/<cityName>')
def test(cityName):
    cityName = url_unquote(cityName)
    annuals = calc_avgs(cityName)
    line = create_plot(annuals)
    title = "Historical Temperature Data for "
    return render_template('test.html', plot=line, cities=g.cities, title=title + cityName, dataName=cityName)
