from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        all_movies = self.session.query(Movie)
        return all_movies.all()

    def get_all_movies_director(self, director_id):
        all_movies = self.session.query(Movie).filter(Director.id == director_id).join(
            Director)
        return all_movies.all()

    def get_all_movies_genre(self, genre_id):
        all_movies = self.session.query(Movie).filter(Genre.id == genre_id).join(Genre)
        return all_movies.all()

    def get_all_movies_year(self, year):
        all_movies = self.session.query(Movie).filter(Movie.year == year)
        return all_movies.all()

    def get_movie(self, uid):
        movie = self.session.query(Movie).get(uid)
        return movie

    def create_movie(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, update):
        self.session.add(update)
        self.session.commit()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
