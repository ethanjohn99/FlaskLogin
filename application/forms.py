from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError 

from application.models import Movies, Review, Accounts

class AccountsCheck: 
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field): 
        all_movies = Accounts.query.all()
        for accounts in all_accounts:
            if accounts.username == field.data:
                raise ValidationError(self.message)

class AccountsForm(FlaskForm):
    username = StringField('User Name',
                validators=[
                    DataRequired(),
                ]
            )
    password = StringField('Password')
    submit = SubmitField('Add User')

class MoviesCheck: 
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field): 
        all_movies = Movies.query.all()
        for movies in all_movies:
            if movies.name == field.data:
                raise ValidationError(self.message)


class MoviesForm(FlaskForm):
    name = StringField('Movie Name',
                validators=[
                    DataRequired(),
                ]
            )
    submit = SubmitField('Add Movie')

class ReviewsCheck: 
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field): 
        all_reviews = Review.query.all()
        for review in all_reviews:
            if review.name == field.data:
                raise ValidationError(self.message)

class ReviewForm(FlaskForm): # customise
    rating = SelectField('Rating',
                choices=[
                    ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')])
    rev = StringField('Review',
                validators=[
                    DataRequired()])
    submit = SubmitField('Add Review')