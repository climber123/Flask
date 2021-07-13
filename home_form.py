from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateHomeForm(FlaskForm):
    basename = StringField('Basename', validators=[DataRequired()])
    submit_del = SubmitField('Del')
    submit_choose = SubmitField('Choose')