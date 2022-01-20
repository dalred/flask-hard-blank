from dao.director_dao import DirectorsDAO
from dao.movie_dao import MoviesDAO
from dao.genre_dao import GenresDAO
from setup_db import db
from service.directors_service import DirectorsService
from service.movies_service import MoviesService
from service.genres_service import GenresService

director_dao = DirectorsDAO(db.session)
director_service = DirectorsService(director_dao)

movie_dao = MoviesDAO(db.session)
movie_service = MoviesService(movie_dao)

genre_dao = GenresDAO(db.session)
genre_service = GenresService(genre_dao)
