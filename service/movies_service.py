from dao.movie_dao import MoviesDAO
from functions import set_keys

#Сервис- Бизнес-Логика
#Views - Сервис  - Dao

class MoviesService:
    def __init__(self, movies_dao: MoviesDAO):
        self.movies_dao = movies_dao

    def get_all_movies(self, director_id, genre_id, year):
        if director_id:
            all_movies = self.movies_dao.get_all_movies_director(director_id)
            return all_movies
        if genre_id:
            all_movies = self.movies_dao.get_all_movies_genre(genre_id)
            return all_movies
        if year:
            all_movies = self.movies_dao.get_all_movies_year(year)
            return all_movies
        all_movies = self.movies_dao.get_all_movies()
        return all_movies


    def get_movie(self, uid):
        movie = self.movies_dao.get_movie(uid)
        return movie


    def create_movie(self, data):
        return self.movies_dao.create_movie(data)


    def update(self, data, uid):
        update = self.get_movie(uid)
        set_keys(data, update)
        self.movies_dao.update(update)


    def delete(self, uid):
        delete_movie = self.get_movie(uid)
        self.movies_dao.delete(delete_movie)