from dao.db_config import get_db_connection
from dto.portfolios_dto import PortfoliosDTO

class PortfoliosDao:
    def __init__(self, connection=None):
        self.connection = connection if connection is not None else get_db_connection()
        self.portfolios = []
        self.total = 0


    def count(self):
        dbcursor = self.connection.cursor()
        dbcursor.execute("SELECT count(*) as Total FROM Portfolios")
        result = dbcursor.fetchall()
        self.total = result[0][0]
        return self.total


    def get_all(self):
        dbcursor = self.connection.cursor()
        dbcursor.execute("SELECT * FROM Portfolios")
        result = dbcursor.fetchall()

        for row in result:
            portfolio = PortfoliosDTO(row[1], row[2], row[0])
            self.portfolios.append(portfolio)
        return self.portfolios
