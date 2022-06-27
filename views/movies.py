from flask import request
from flask_restx import Resource, Namespace
from dao.model.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    schema = MovieSchema(many=True)

    def get(self):
        movies = self.schema.dump(movie_service.get_movies(**request.args))
        return movies, 200

    def post(self):
        """ Создание нового объекта в таблице Movie"""
        new_movie = movie_service.create_movie(request.json)
        return "", 201, {'location': f"{movie_ns.path}/{new_movie.id}"}


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    schema = MovieSchema()

    def get(self, uid: int):
        """ Вывод информации о фильме по id."""
        return self.schema.dump(movie_service.get_movies(uid)), 200

    def patch(self, uid: int):
        """ Частичное изменение информации о фильме. """
        return self.schema.dump(movie_service.update_part(uid, request.json)), 200

    def put(self, uid: int):
        """ Полное изменение информации о фильме. """
        return self.schema.dump(movie_service.update_full(uid, request.json)), 200

    def delete(self, uid: int):
        """ Удаление фильма по id. """
        movie_service.delete(uid)
        return "", 204
