from flask_restx import Resource, Namespace
from dao.model.directors import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    schema = DirectorSchema(many=True)
    def get(self):
        """ Вывод всех режиссеров"""
        return self.schema.dump(director_service.get_directors()), 200


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    schema = DirectorSchema()
    def get(self, uid):
        """ Вывод режиссера по id"""
        return self.schema.dump(director_service.get_directors(uid)), 200

