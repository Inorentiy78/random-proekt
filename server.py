from flask import Flask, render_template , jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class GenreMovie(db.Model):
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    created_data = db.Column(db.DateTime(timezone=True))  
    genres = db.relationship('Genre', secondary=GenreMovie.__table__,lazy='subquery', backref= db.backref('movies', lazy=True))
    image_url = db.Column(db.String, nullable=False)




@app.route("/")
def index():
    genres = Genre.query.all()
    movies = Movie.query.all()
    genremovies = GenreMovie.query.all()
    return render_template("index.html", genres=genres , movies = movies , genremovies = genremovies)

@app.route('/get_movie/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie is not None:
        return jsonify({
            'title': movie.title,
            'city': movie.city,
            'created_data': movie.created_data.strftime("%Y-%m-%d"),
            'description': movie.description,
            'image_url': movie.image_url
        })
    else:
        return jsonify({'error': 'Фильм не найден'})


if __name__ == '__main__':
    app.run(debug=True)