from dao.director_dao import DirectorsDAO
from functions import set_keys

#Сервис- Бизнес-Логика
#Views - Сервис  - Dao

class DirectorsService:
    def __init__(self, directors_dao: DirectorsDAO):
        self.directors_dao = directors_dao

    def get_all_directors(self):
        all_directors = self.directors_dao.get_all_directors()
        return all_directors


    def get_director(self, uid):
        director = self.directors_dao.get_director(uid)
        return director


    def create_director(self, data):
        return self.directors_dao.create_director(data)


    def update(self, data, uid):
        update = self.get_director(uid)
        set_keys(data, update)
        self.directors_dao.update(update)


    def delete(self, uid):
        delete_director = self.get_director(uid)
        self.directors_dao.delete(delete_director)