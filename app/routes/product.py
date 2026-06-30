from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import jwt
from app.services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
    search_products,
    get_products_by_category,
    get_products_by_supplier
)

# Create a Blueprint for product routes
product_bp = Blueprint('product_bp', __name__, url_prefix='/api/products')

@product_bp.route('/', methods=['GET'])
def get_products_route():
    """Fetch all products or search by name if a query parameter is provided."""
    name_query = request.args.get('name')
    if name_query:
        products = search_products(name_query)
    else:
        products = get_all_products()
    return jsonify(products), 200

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product_route(product_id):
    """Fetch a single product by its ID."""
    product, error = get_product_by_id(product_id)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(product), 200

@product_bp.route('/', methods=['POST'])
@jwt_required()
def create_product_route():
    """Create a new product."""
    data = request.get_json()
    
    # Basic validation to ensure required fields exist
    required_fields = ['product_name', 'price', 'category_id', 'supplier_id']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
        
    product, error = create_product(data)
    return jsonify(product), 201

@product_bp.route('/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product_route(product_id):
    """Update an existing product."""
    data = request.get_json()
    product, error = update_product(product_id, data)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(product), 200

@product_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product_route(product_id):
    """Delete a product by its ID."""
    result, error = delete_product(product_id)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(result), 200

@product_bp.route('/category/<int:category_id>', methods=['GET'])
def get_products_by_category_route(category_id):
    """Fetch all products belonging to a specific category."""
    products = get_products_by_category(category_id)
    return jsonify(products), 200

@product_bp.route('/supplier/<int:supplier_id>', methods=['GET'])
def get_products_by_supplier_route(supplier_id):
    """Fetch all products belonging to a specific supplier."""
    products = get_products_by_supplier(supplier_id)
    return jsonify(products), 200