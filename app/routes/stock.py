from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.stock_service import (
    get_stock_by_products, create_stock_for_product,
    stock_in, stock_out, get_low_stock_products
)

stock_bp = Blueprint('stock', __name__, url_prefix='/api/stock')

@stock_bp.route('/product/<int:product_id>', methods=['GET'])
@jwt_required()
def get_stock(product_id):
    stock, error = get_stock_by_products(product_id)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(stock), 200

@stock_bp.route('/create', methods=['POST'])
@jwt_required()
def create_stock():
    data = request.get_json()
    if not data or 'product_id' not in data:
        return jsonify({"error": "product_id is required"}), 400
    
    stock, error = create_stock_for_product(
        data['product_id'],
        data.get('initial_quantity', 0)
    )
    if error:
        return jsonify({"error": error}), 409
    return jsonify(stock), 201

@stock_bp.route('/in', methods=['POST'])
@jwt_required()
def add_stock():
    data = request.get_json()
    if not data or 'product_id' not in data or 'quantity' not in data:
        return jsonify({"error": "product_id and quantity are required"}), 400
    
    stock, error = stock_in(data['product_id'], int(data['quantity']))
    if error:
        return jsonify({"error": error}), 404
    return jsonify(stock), 200

@stock_bp.route('/out', methods=['POST'])
@jwt_required()
def remove_stock():
    data = request.get_json()
    if not data or 'product_id' not in data or 'quantity' not in data:
        return jsonify({"error": "product_id and quantity are required"}), 400
    
    stock = stock_out(data['product_id'], int(data['quantity']))
    
    return jsonify(stock), 200

@stock_bp.route('/low-stock', methods=['GET'])
@jwt_required()
def get_low_stock():
    threshold = request.args.get('threshold', 10, type=int)
    low_stock = get_low_stock_products(threshold)
    return jsonify(low_stock), 200