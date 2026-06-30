import bcrypt
from app import db
from app.models.user import User
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
def verify_password(password, hashed):
    return  bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
def register_user(data):
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return None, "Email already registered"
    hashed_pw = hash_password(data['password'])
    new_user = User(
        name = data['name'],
        email = data['email'],
        password =hashed_pw,
        role = data.get('role', 'staff')

    )
    db.session.add(new_user)
    db.session.commit()
    return new_user, None
def login_user(data):
    user = User.query.filter_by(email= data['email']).first()
    if not user:
        return None, "user not found"
    if not verify_password(data['password'], user.password):
        return None, "Invaild password"
    return user, None
