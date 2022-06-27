from dao.model.directors import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get(self, gid=None):
        query = self.session.query(Director)
        if gid:
            return query.get(gid)
        else:
            return query.all()
