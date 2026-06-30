from app import db
from app.models.category import Category
def get_all_cattegories():
    categories = Category.query.all()
    return [{"id": c.id, "category_name":c.category_name} for c in categories]
def get_category_by_id(category_id):
    category = Category.query.get(category_id)
    if not category:
        return None, "Category not found"
    return {"id":category.id, "category_name": category.category_name}, None
def create_category(data):
    existing = Category.query.filter_by(category_name = data['category_name']).first()
    if existing:
        return None, "Category already exists"
    category = Category(category_name=data['category_name'])
    db.session.add(category)
    db.session.commit()
    return {"id": category.id, "category_name": category.category_name}
def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return None, "Category not found"
    db.session.delete(category)
    db.session.commit()
    return {"message": "Category deleted"}, None
def update_category(category_id, data):
    category = Category.query.get(category_id)
    if not category:
        return None, "Category not found"
    
    category.category_name =  data.get('category_name', category.category_name)
    db.session.commit()
    return {"id": category.id, "category__name":category.category_name}, None

        
    
