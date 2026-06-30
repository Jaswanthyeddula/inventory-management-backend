from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.services.dashboard_service import(
    get_dashboard_summary,
    get_reccent_transaction
    
)
dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')
@dashboard_bp.route('/summary', methods=['GET'])
@jwt_required()
def summary():
    result= get_dashboard_summary()
    return jsonify(result), 200
@dashboard_bp.route('/transactions', methods=['GET'])
@jwt_required()
def transaction_route():
    result = get_reccent_transaction()
    return jsonify(result), 200