from app import db
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String(100), unique=True, nullable=False)

    # products = db.relationship('Product', backref='category', lazy=True, foreign_keys = 'Product.ctegory_id')