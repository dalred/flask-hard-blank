from dao.genre_dao import GenresDAO
from functions import set_keys

#Сервис- Бизнес-Логика
#Views - Сервис  - Dao

class GenresService:
    def __init__(self, genres_dao: GenresDAO):
        self.genres_dao = genres_dao

    def get_all_genres(self):
        all_genres = self.genres_dao.get_all_genres()
        return all_genres


    def get_genre(self, uid):
        genre = self.genres_dao.get_genre(uid)
        return genre


    def create_genre(self, data):
        return self.genres_dao.create_genre(data)


    def update(self, data, uid):
        update = self.get_genre(uid)
        set_keys(data, update)
        self.genres_dao.update(update)


    def delete(self, uid):
        delete_genre = self.get_genre(uid)
        self.genres_dao.delete(delete_genre)