from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_movies(self, mid=None, **kwargs):
        return self.dao.get(mid, **kwargs)

    def create_movie(self, data):
        return self.dao.create(data)

    def update_full(self, uid, data):
        movie = self.get_movies(uid)
        movie.title = data['title']
        movie.description = data['description']
        movie.rating = data['rating']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        self.dao.update(movie)
        return movie

    def update_part(self, uid, data):
        movie = self.get_movies(uid)
        if 'title' in data:
            movie.title = data['title']
        if 'description' in data:
            movie.description = data['description']
        if 'rating' in data:
            movie.rating = data['rating']
        if 'trailer' in data:
            movie.trailer = data['trailer']
        if 'year' in data:
            movie.year = data['year']
        if 'genre_id' in data:
            movie.genre_id = data['genre_id']
        if 'director_id' in data:
            movie.director_id = data['director_id']
        self.dao.update(movie)
        return movie

    def delete(self, movie_id):
        """ Удаление фильма по id. """
        self.dao.delete(movie_id)

    def filter_by_genre(self, genre_id):
        movies = self.get_movies()
        result = []
        for movie in movies:
            if movie.genre_id == int(genre_id):
                result.append(movie)
        return result
