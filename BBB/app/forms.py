from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import ValidationError, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from app.models import City, Weather

class FileForm(FlaskForm):
    file = FileField('City Weather File', validators=[
        FileRequired(),
        FileAllowed(['csv'], 'csv file only')
    ])
    city_name = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Upload')
