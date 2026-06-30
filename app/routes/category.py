from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.services.category_service import (
    get_all_cattegories,
    get_category_by_id,
    create_category,
    delete_category,
    update_category
)
category_bp = Blueprint('category', __name__, url_prefix='/api/categories')
@category_bp.route('/', methods=['GET'])
@jwt_required()
def get_categories():
    categories = get_all_cattegories()
    return jsonify(categories), 200
@category_bp.route('/<int:category_id>', methods=['GET'])
@jwt_required()
def get_category(category_id):
    category, error = get_category_by_id(category_id)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(category), 200
@category_bp.route('/', methods=['POST'])
@jwt_required()
def create_category_route():
    data = request.get_json()
    if not data or 'category_name' not in data:
        return jsonify ({"error": "category_name is required"}), 400
    category= create_category(data)
    if not category:
        return jsonify({"error": "An error occured"}), 409
    return jsonify(category), 201
@category_bp.route('/<int:category_id>', methods=['PUT'])
@jwt_required()
def update_category(category_id):
    data = request.get_json()
    category, error = update_category(category_id, data)
    if error:
        return jsonify({"error": error}), 409
    return jsonify(category), 200
@category_bp.route('/<int:category_id>', methods=['DELETE'])
@jwt_required()
def delete_category(category_id):
    result, error = delete_category(category_id)
    if error:
        return jsonify({"error": error}), 409
    return jsonify(result), 200
