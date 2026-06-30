from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from app.services.auth_service import register_user, login_user
from app import limiter

auth_bp = Blueprint('auth',__name__, url_prefix='/api/auth')
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not all(k in data for k in ('name','email','password')):
        return jsonify({"error":"name,email,password are required"})
    user, error = register_user(data)
    if error:
        return jsonify({"error": error}), 409
    return jsonify({"message":"user registred successfully"})
@auth_bp.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    data = request.get_json()
    if not data or not all(k in data for k in ('email','password')):
        return jsonify({"error":"email,password are required"})
    user, error = login_user(data)
    if error:
        return jsonify({"error": error}), 401
    access_token = create_access_token(identity=str(user.id))
    return jsonify({
        "message":"login successful",
        "token":access_token,
        "user":{
            "id":user.id,
            "name":user.name,
            "email":user.email,
            "role":user.role

        }
    }), 200
