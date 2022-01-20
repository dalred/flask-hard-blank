from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema
from flask import request, jsonify, make_response


movies_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)



@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        return make_response(jsonify(movies_schema.dump(movie_service.get_all_movies(director_id, genre_id, year))), 200)

    def post(self):
        req_json = request.json
        movie = movie_service.create_movie(req_json)
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f"/movies/{movie.id}/"
        response.autocorrect_location_header = False
        return response


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        return make_response(jsonify(movie_schema.dump(movie_service.get_movie(uid))), 200)

    def put(self, uid: int):
        req_json = request.json
        movie_service.update(req_json, uid)
        return "", 204

    def delete(self, uid: int):
        movie_service.delete(uid)
        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        movie_service.update(req_json, uid)
        return "", 204