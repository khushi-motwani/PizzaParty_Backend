from service.assets_service import AssetsService
from flask import Blueprint, jsonify

assets_bp = Blueprint('assets', __name__, url_prefix='/assets')

assets_service = AssetsService()

@assets_bp.route('/all', methods=['GET'])
def get_all_assets():
    assets = assets_service.get_all()
    return jsonify([asset.to_dict() for asset in assets])

@assets_bp.route('/count', methods=['GET'])
def get_assets_count():
    count = assets_service.count()
    return jsonify({"count": count})
