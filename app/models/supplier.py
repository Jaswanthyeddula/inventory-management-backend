from app import db
class Supplier(db.Model):
    __tablename__ = 'suppliers'
    id = db.Column(db.Integer, primary_key = True)
    supplier_name = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    address = db.Column(db.Text)

    # products  = db.relationship('Product', backref='supplier', lazy=True, foreign_keys = 'Product.supplier_id')