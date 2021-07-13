from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateChoosenForm(FlaskForm):
    execute = StringField('Execute', validators=[DataRequired()])
    submit = SubmitField('Start')