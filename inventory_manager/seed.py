from .database import Session, init_db
from .models import Supplier, Product

def seed_data():
    init_db()
    session = Session()
    
    # Add sample suppliers
    suppliers = [
        Supplier(name="Tech Corp", contact_info="tech@corp.com"),
        Supplier(name="Office Supply Co", contact_info="office@supply.com")
    ]
    
    for supplier in suppliers:
        session.add(supplier)
    session.commit()
    
    # Add sample products
    products = [
        Product(name="Laptop", price=999.99, quantity_in_stock=10, supplier_id=1),
        Product(name="Mouse", price=25.50, quantity_in_stock=50, supplier_id=1),
        Product(name="Desk Chair", price=199.99, quantity_in_stock=5, supplier_id=2)
    ]
    
    for product in products:
        session.add(product)
    session.commit()
    
    print("Sample data added successfully!")
    session.close()

if __name__ == '__main__':
    seed_data()