from service.transactions_service import TransactionsService
from flask import Blueprint, jsonify

transactions_bp = Blueprint('transactions', __name__, url_prefix='/transactions')

transactions_service = TransactionsService()

def set_transactions_service(service):
    global transactions_service
    transactions_service = service

@transactions_bp.route('/all', methods=['GET'])
def get_all_transactions():
    transactions = transactions_service.get_all()
    return jsonify([transaction.to_dict() for transaction in transactions])

@transactions_bp.route('/count', methods=['GET'])
def get_transactions_count():
    count = transactions_service.count()
    return jsonify({"count": count})
