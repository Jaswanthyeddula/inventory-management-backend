# from app import db
# from app.models.product import Product

# def get_all_products():
#     products = Product.query.all()
#     return [{
#         "id": p.id,
#         "product_name": p.product_name,
#         "description": p.description,
#         "price": p.price,
#         "category_id": p.category_id,
#         "supplier_id": p.supplier_id,
#         "created_at": p.created_at.isoformat() if p.created_at else None
#     } for p in products]

# def get_product_by_id(product_id):
#     product = Product.query.get(product_id)
#     if not product:
#         return None, "Product not found"
#     return {
#         "id": product.id,
#         "product_name": product.product_name,
#         "description": product.description,
#         "price": product.price,
#         "category_id": product.category_id,
#         "supplier_id": product.supplier_id,
#         "created_at": product.created_at.isoformat() if product.created_at else None
#     }, None

# def create_product(data):
#     product = Product(
#         product_name=data['product_name'],
#         description=data.get('description'),
#         price=data['price'],
#         category_id=data['category_id'],
#         supplier_id=data['supplier_id']
#     )
#     db.session.add(product)
#     db.session.commit()
#     return {
#         "id": product.id,
#         "product_name": product.product_name,
#         "description": product.description,
#         "price": product.price,
#         "category_id": product.category_id,
#         "supplier_id": product.supplier_id,
#         "created_at": product.created_at.isoformat() if product.created_at else None
#     }, None

# def update_product(product_id, data):
#     product = Product.query.get(product_id)
#     if not product:
#         return None, "Product not found"
    
#     product.product_name = data.get('product_name', product.product_name)
#     product.description = data.get('description', product.description)
#     product.price = data.get('price', product.price)
#     product.category_id = data.get('category_id', product.category_id)
#     product.supplier_id = data.get('supplier_id', product.supplier_id)
#     db.session.commit()
#     return {
#         "id": product.id,
#         "product_name": product.product_name,
#         "description": product.description,
#         "price": product.price,
#         "category_id": product.category_id,
#         "supplier_id": product.supplier_id,
#         "created_at": product.created_at.isoformat() if product.created_at else None
#     }, None

# def delete_product(product_id):
#     product = Product.query.get(product_id)
#     if not product:
#         return None, "Product not found"
#     db.session.delete(product)
#     db.session.commit()
#     return {"message": "Product deleted successfully"}, None

# def search_products(name):
#     products = Product.query.filter(Product.product_name.ilike(f"%{name}%")).all()
#     return [{
#         "id": p.id,
#         "product_name": p.product_name,
#         "description": p.description,
#         "price": p.price,
#         "category_id": p.category_id,
#         "supplier_id": p.supplier_id,
#         "created_at": p.created_at.isoformat() if p.created_at else None
#     } for p in products]

# def get_products_by_category(category_id):
#     products = Product.query.filter_by
from app import db
from app.models.product import Product

def get_all_products():
    products = Product.query.all()
    return [p.to_dict() for p in products]

def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None, "Product not found"
    return product.to_dict(), None

def create_product(data):
    product = Product(
        product_name=data['product_name'],
        description=data.get('description'),
        price=data['price'],
        category_id=data['category_id'],
        supplier_id=data['supplier_id']
    )
    db.session.add(product)
    db.session.commit()
    return product.to_dict(), None

def update_product(product_id, data):
    product = Product.query.get(product_id)
    if not product:
        return None, "Product not found"
    
    product.product_name = data.get('product_name', product.product_name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.category_id = data.get('category_id', product.category_id)
    product.supplier_id = data.get('supplier_id', product.supplier_id)
    
    db.session.commit()
    return product.to_dict(), None

def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None, "Product not found"
    
    db.session.delete(product)
    db.session.commit()
    return {"message": "Product deleted successfully"}, None

def search_products(name):
    products = Product.query.filter(Product.product_name.ilike(f"%{name}%")).all()
    return [p.to_dict() for p in products]

def get_products_by_category(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    return [p.to_dict() for p in products]

def get_products_by_supplier(supplier_id):
    products = Product.query.filter_by(supplier_id=supplier_id).all()
    return [p.to_dict() for p in products]