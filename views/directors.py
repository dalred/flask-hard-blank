from flask_restx import Resource, Namespace

from container import director_service
from dao.model.director import DirectorSchema
from flask import request, jsonify, make_response

directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return make_response(jsonify(directors_schema.dump(director_service.get_all_directors())), 200)

    def post(self):
        req_json = request.json
        director = director_service.create_director(req_json)
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f"/directors/{director.id}/"
        response.autocorrect_location_header = False
        return response


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        return make_response(jsonify(director_schema.dump(director_service.get_director(uid))), 200)

    def put(self, uid: int):
        req_json = request.json
        director_service.update(req_json, uid)
        return "", 204

    def delete(self, uid: int):
        director_service.delete(uid)
        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        director_service.update(req_json, uid)
        return "", 204
