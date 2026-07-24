from dao.db_config import get_db_connection
from dto.transactions_dto import TransactionsDTO

class TransactionsDao:
    def __init__(self, connection_factory=None):
        self.connection_factory = connection_factory or get_db_connection
        self.connection = None
        self.transactions = []
        self.total = 0

    def _get_connection(self):
        if self.connection is None:
            self.connection = self.connection_factory()
        return self.connection

    def count(self):
        dbcursor = self._get_connection().cursor()
        dbcursor.execute("SELECT count(*) as Total FROM Transactions")
        result = dbcursor.fetchall()
        self.total = result[0][0]
        return self.total


    def get_all(self):
        dbcursor = self._get_connection().cursor()
        dbcursor.execute("SELECT * FROM Transactions")
        result = dbcursor.fetchall()

        for row in result:
            transaction = TransactionsDTO(row[1], row[3], row[4], row[6], row[7], row[8], row[0], row[2], row[5])
            self.transactions.append(transaction)
        return self.transactions
