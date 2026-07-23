from dao.assets_dao import AssetsDao

class AssetsService:
    def __init__(self):
        self.assets_dao = AssetsDao()

    def get_all(self):
        return self.assets_dao.get_all()

    def count(self):
        return self.assets_dao.count()
