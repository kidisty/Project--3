from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LegoPrefForm(FlaskForm):
    piece_count = IntegerField('Piece Count', validators=[DataRequired()])
    difficulty = IntegerField('Difficulty (1-5)', validators=[DataRequired()])
    star_rating = IntegerField('Rating (1-5)', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit Lego Preferences')
