from dao.model.genre import Genre

class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        all_genres = self.session.query(Genre).all()
        return all_genres

    def get_genre(self, uid):
        genre = self.session.query(Genre).get(uid)
        return genre

    def create_genre(self, data):
        new_genre = Genre(**data)
        self.session.add(new_genre)
        self.session.commit()
        return new_genre

    def update(self, update):
        self.session.add(update)
        self.session.commit()


    def delete(self, genre):
        self.session.delete(genre)
        self.session.commit()
