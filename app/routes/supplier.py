from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.supplier_service import (
    get_all_suppliers,
    get_supplier_by_id,
    create_supplier,
    update_supplier,
    delete_supplier

)
supplier_bp = Blueprint('supplier', __name__, url_prefix='/api/suppliers')

@supplier_bp.route('/', methods=['GET'])
@jwt_required()
def get_suppliers_route():
    return jsonify(get_all_suppliers()), 200
@supplier_bp.route('/<int:supplier_id>', methods=['GET'])
@jwt_required()
def get_supplier(supplier_id):
    supplier, error = get_supplier_by_id(supplier_id)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(supplier), 200
@supplier_bp.route('/', methods=['POST'])
@jwt_required()
def create_supplier_route():
    data =  request.get_json()
    if not data or 'supplier_name' not in data :
        return jsonify ({"error": "supplier name is required"}), 400
    result, error = create_supplier(data)
    if error:
        return jsonify({"error": error}), 400
    return jsonify (result), 201
@supplier_bp.route('/<int:supplier_id>', methods=['PUT'])
@jwt_required()
def update_supplie_route(supplier_id):
    data = request.get_json()
    supplier, error = update_supplier(supplier_id, data)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(supplier),  200
@supplier_bp.route('/<int:supplier_id>', methods=['DELETE'])
@jwt_required()
def delete_supplier_route(supplier_id):
    result = delete_supplier(supplier_id)
    if not result:
        return jsonify ({"error": "it is not found"}),  404
    return jsonify(result), 200