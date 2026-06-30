from app import db
from app.models.supplier import Supplier
def get_all_suppliers():
    suppliers = Supplier.query.all()
    return [{
        "id": s.id,
        "supplier_name":s.supplier_name,
        "phone":s.phone,
        "email":s.email,
        "address":s.address
    } for s in suppliers]
def get_supplier_by_id(supplier_id):
    supplier  = Supplier.query.get(supplier_id)
    if not supplier:
        return None, "Supplier not found"
    return{
        "id": supplier.id,
        "supplier_name": supplier.supplier_name,
        "phone": supplier.phone,
        "email": supplier.email,
        "address": supplier.address
    }, None
def create_supplier(data):
    if not data.get('supplier_name'):
        return None, "Supplier name is required"
    if not data.get('phone'):
        return None, "Supplier phone is required"
    if not data.get('address'):
        return None, "Supplier address is required"
    if not data.get('email'):
        return None, "Supplier email is required"
    supplier = Supplier (
        supplier_name = data['supplier_name'],
        phone = data.get('phone'),
        email = data.get('email'),
        address = data.get('address')
   
    )
    db.session.add(supplier)
    db.session.commit()
    
    return {
        "id": supplier.id,
        "supplier_name": supplier.supplier_name,
        "phone": supplier.phone,
        "email": supplier.email,
        "address": supplier.address

    }, None
def update_supplier(supplier_id, data):
    supplier = Supplier.query.get(supplier_id)
    if not supplier:
        return None, "supplier not found"
    supplier.supplier_name  = data('supplier_name', supplier.supplier_name),
    supplier.phone = data('phone', supplier.phone)
    supplier.email = data('email', supplier.email)
    supplier.address = data('address', supplier.address)
    db.session.commit()
    return {
        "id": supplier.id,
        "supplier_name": supplier.supplier_name,
        "phone": supplier.phone,
        "email": supplier.email,
        "address": supplier.address

    }, None
def delete_supplier(supplier_id):
    supplier = Supplier.query.get(supplier_id)
    if not supplier:
        return None, "supplier is not found"
    db.session.delete(supplier)
    db.session.commit()
    return {"message":"Supplier deleted successfully"}
