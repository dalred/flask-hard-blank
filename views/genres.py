from flask_restx import Resource, Namespace

from container import genre_service
from dao.model.genre import GenreSchema
from flask import request, jsonify, make_response

genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        return make_response(jsonify(genres_schema.dump(genre_service.get_all_genres())), 200)

    def post(self):
        req_json = request.json
        genre = genre_service.create_genre(req_json)
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f"/genres/{genre.id}/"
        response.autocorrect_location_header = False
        return response


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        return make_response(jsonify(genre_schema.dump(genre_service.get_genre(uid))), 200)

    def put(self, uid: int):
        req_json = request.json
        genre_service.update(req_json, uid)
        return "", 204

    def delete(self, uid: int):
        genre_service.delete(uid)
        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        genre_service.update(req_json, uid)
        return "", 204
