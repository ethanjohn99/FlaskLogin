from application import db
from application.models import Movies

db.drop_all()
db.create_all()

new_movie = Movies(name = "Citizen Kane, Thriller, Orson Welles: ")
db.session.add(new_movie)

db.session.commit()
