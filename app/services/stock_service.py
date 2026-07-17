import threading

from app import db
from app.models.supplier import Supplier
from app.services.email_service import send_warning_email
from app.models.stock import Stock
from app.models.stock_in import StockIn
from app.models.stock_out import StockOut
from app.models.product import Product
def  get_stock_by_products(product_id):
    stock = Stock.query.filter_by(product_id=product_id).first()
    if not stock:
        return None, "Stock not found"
    return{
        "id":stock.id,
        "product_id":stock.product_id,
        "quantity":stock.quantity,
        "last_updated": stock.last_updated

        }, None
def create_stock_for_product(product_id, intial_quantity=0):
    existing = Stock.query.filter_by(product_id=product_id).first()
    if existing:
        return None, "Stock  already exists"
    stock = Stock(product_id=product_id, quantity=intial_quantity)
    db.session.add(stock)
    db.session.commit()
    return {
        "id":stock.id,
        "product_id":stock.product_id,
        "quantity":stock.quantity,
        "last_updated": stock.last_updated

    
    }, None
def stock_in(product_id, quantity):
    stock = Stock.query.filter_by(product_id=product_id).first()
    if not stock:
        stock = Stock(product_id=product_id, quantity=0)
        db.session.add(stock)
    stock.quantity += int(quantity)
    db.session.commit()
    stock_in_record = StockIn(product_id=product_id, quantity=int(quantity))
    db.session.add(stock_in_record)
    db.session.commit()
    return {
        "id":stock.id,
        "product_id":stock.product_id,
        "quantity":stock.quantity,
        "last_updated": stock.last_updated

    
    }, None
def stock_out(product_id, quantity):
    stock = Stock.query.filter_by(product_id=product_id).first()
    product_record = Product.query.get(product_id)
    if not stock:
        return None, "Stock not found for this product"
    if stock.quantity < int(quantity):
        return None, f"Insufficent Stock. Available: {stock.quantity}"
    stock.quantity -= int(quantity)

    stock_out_record = StockOut(product_id=product_id, quantity=quantity)
    db.session.add(stock_out_record)
    db.session.commit()
    try:
        if stock.quantity < 10:
            supplier = Supplier.query.get(product_record.supplier_id)
        if supplier:
        
            email_thread = threading.Thread(
                target=send_warning_email,
                kwargs={
                    "item_name": product_record.product_name,
                    "items_left": stock.quantity,
                    "supplier_email": supplier.email
                }
            )
            email_thread.start()
            print(f"WARNING: Low stock for {product_record.product_name}. Email sent to {supplier.email}")
        else:
            print(f"WARNING: Low stock for {product_record.product_name}. No supplier email found.")
            
    except Exception as e:
        print(f"Email failed to send: {e}")
       
    db.session.commit()
    
    
    return {
        "id":stock.id,
        "product_id":stock.product_id,
        "quantity":stock.quantity,
        "last_updated": str(stock.last_updated)

    
    }, None



def get_low_stock_products(thersold=10):
    low_stock = Stock.query.filter(Stock.quantity < thersold ).all()
    return [{
        "id":s.id,
        "product_id":s.product_id,
        "quantity":s.quantity,
        "last_updated":s.last_updated.isoformat() if s.last_updated else None

    } for s in low_stock]