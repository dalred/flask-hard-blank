from flask_restx import Api
from flask import Flask
from config import Config
from setup_db import db
from create_tables import create_db_in_memory
import prettytable
from views.directors import directors_ns
from views.movies import movies_ns
from views.genres import genres_ns

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    create_data(app)


def create_data(app):
    with app.app_context():
        create_db_in_memory()

app = create_app(Config())
app.debug = True

INSTANCE_movie = {
    "description": "Тест",
    "rating": 7.8,
    "title": "Тест",
    "trailer": "Тест",
    "year": 2022,
    "genre_id":17,
    "director_id":1
}

POST = {
    "name": "Тест"
}

patch = {
    "name": "Тест",
    "name2": "ТестТест"
}

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
    # client = app.test_client()  # TODO вы можете раскомментировать
    # response = client.post('/movies/', json=INSTANCE_movie)
    # with app.app_context():
    #     session = db.session()  # свой json в соответствующий аргумент
    #     cursor = session.execute("SELECT * FROM movie").cursor  # функции post
    #     mytable = prettytable.from_db_cursor(cursor)
    #     mytable.max_width = 30
    #     print("БАЗА ДАННЫХ")
    #     print(mytable)
