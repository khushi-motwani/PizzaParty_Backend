from service.portfolios_service import PortfoliosService
from flask import Blueprint, jsonify

portfolios_bp = Blueprint('portfolios', __name__, url_prefix='/portfolios')

portfolios_service = PortfoliosService()

@portfolios_bp.route('/all', methods=['GET'])
def get_all_portfolios():
    portfolios = portfolios_service.get_all()
    return jsonify([portfolio.to_dict() for portfolio in portfolios])

@portfolios_bp.route('/count', methods=['GET'])
def get_portfolios_count():
    count = portfolios_service.count()
    return jsonify({"count": count})
