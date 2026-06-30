from app import db
from datetime import datetime
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    # stocks = db.relationship('Stock', backref='product', cascade="all, delete-orphan")
    # stock_ins = db.relationship('Stock_In', backref='product', cascade="all, delete-orphan")
    # stock_outs = db.relationship('Stock_Out', backref='product', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "description": self.description,
            "price": self.price,
            "category_id": self.category_id,
            "supplier_id": self.supplier_id,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
    # stock = db.relationship('Stock', backref='product', uselist=False, lazy=True)
    # stock_in = db.relationship('Stock_In', backref='product', lazy=True)
    # stock_out = db.relationship('Stock_Out', backref='product', lazy=True)
