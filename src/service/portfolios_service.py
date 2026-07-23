from dao.portfolios_dao import PortfoliosDao

class PortfoliosService:
    def __init__(self):
        self.portfolios_dao = PortfoliosDao()

    def get_all(self):
        return self.portfolios_dao.get_all()

    def count(self):
        return self.portfolios_dao.count()
