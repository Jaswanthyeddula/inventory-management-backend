from app import db
from app.models.product import Product
from app.models.category import Category
from app.models.supplier import Supplier
from app.models.stock import Stock
from app.models.stock_in import StockIn
from app.models.stock_out import StockOut
from sqlalchemy import func
def get_dashboard_summary():
    total_products = Product.query.count()
    total_suppliers = Supplier.query.count()
    total_categories = Category.query.count()
    low_stock_count = Stock.query.filter(Stock.quantity < 10).count()
    total_inventory_value = db.session.query(
        func.sum(Product.price * Stock.quantity)
    ).join(Stock, Product.id == Stock.product_id).scalar() or 0.0
    return{
        "total_products":total_products,
        "total_suppliers":total_suppliers,
        "total_categories":total_categories,
        "low_stock_count":low_stock_count,
        "total_inventory_value":total_inventory_value
    }
def get_reccent_transaction():
    stock_in_record = StockIn.query.order_by(StockIn.date.desc()).limit(5).all()
    stock_out_record = StockOut.query.order_by(StockOut.date.desc()).limit(5).all()

    transactions=[]
    for record in stock_in_record:
        transactions.append({
            "id":record.id,
            "product_id":record.product_id,
            "quantity":record.quantity,
            "type":"IN",
            "date":record.date.isoformat()
        })
    for record in stock_out_record:
        transactions.append({
            "id":record.id,
            "product_id":record.product_id,
            "quantity":record.quantity,
            "type":"OUT",
            "date":record.date.isoformat()
        })
    transactions.sort(key=lambda x: x["date"], reverse=True)
    recent_top_5 = transactions[:5]
    return recent_top_5