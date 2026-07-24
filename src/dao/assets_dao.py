from dao.db_config import get_db_connection
from dto.assets_dto import AssetsDTO

class AssetsDao:
    def __init__(self, connection_factory=None):
        self.connection_factory = connection_factory or get_db_connection
        self.connection = None
        self.assets = []
        self.total = 0

    def _get_connection(self):
        if self.connection is None:
            self.connection = self.connection_factory()
        return self.connection

    def count(self):
        dbcursor = self._get_connection().cursor()
        dbcursor.execute("SELECT count(*) as Total FROM Assets")
        result = dbcursor.fetchall()
        self.total = result[0][0]
        return self.total


    def get_all(self):
        dbcursor = self._get_connection().cursor()
        dbcursor.execute("SELECT * FROM Assets")
        result = dbcursor.fetchall()

        for row in result:
            asset = AssetsDTO(row[1], row[2], row[3], row[4], row[5], row[0])
            self.assets.append(asset)
        return self.assets
