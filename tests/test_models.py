import unittest
from inventory_manager.database import Session, init_db
from inventory_manager.models import Supplier, Product, Order

class TestModels(unittest.TestCase):
    
    def setUp(self):
        init_db()
        self.session = Session()
    
    def tearDown(self):
        self.session.close()
    
    def test_supplier_creation(self):
        supplier = Supplier(name="Test Corp", contact_info="test@corp.com")
        self.assertEqual(supplier.name, "Test Corp")
        self.assertEqual(supplier.contact_info, "test@corp.com")
    
    def test_product_creation(self):
        product = Product(name="Test Product", price=99.99, quantity_in_stock=10, supplier_id=1)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 99.99)

if __name__ == '__main__':
    unittest.main()