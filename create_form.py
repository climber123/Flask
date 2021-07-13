from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateAddForm(FlaskForm):
    basename = StringField('Basename', validators=[DataRequired()])
    execute = StringField('Execute', validators=[DataRequired()])
    submit = SubmitField('Start')