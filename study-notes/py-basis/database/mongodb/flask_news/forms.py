from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class NewsForm(FlaskForm):
    title = StringField()
    content = TextAreaField()
    types = SelectField()
    image = StringField()
    submit = SubmitField()