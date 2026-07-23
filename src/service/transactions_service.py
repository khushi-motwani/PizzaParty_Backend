from dao.transactions_dao import TransactionsDao

class TransactionsService:
    def __init__(self):
        self.transactions_dao = TransactionsDao()

    def get_all(self):
        return self.transactions_dao.get_all()

    def count(self):
        return self.transactions_dao.count()
