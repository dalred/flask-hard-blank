# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД


from dao.model.director import Director

class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        all_directors = self.session.query(Director).all()
        return all_directors

    def get_director(self, uid):
        director = self.session.query(Director).get(uid)
        return director

    def create_director(self, data):
        new_director = Director(**data)
        self.session.add(new_director)
        self.session.commit()
        return new_director

    def update(self, update):
        self.session.add(update)
        self.session.commit()


    def delete(self, director):
        self.session.delete(director)
        self.session.commit()
