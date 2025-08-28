#!/usr/bin/env python3
import argparse
from .database import Session, init_db
from .models import Product, Supplier, Order
from tabulate import tabulate

def add_product(name, price, supplier_id, stock=0):
    session = Session()
    product = Product(name=name, price=price, supplier_id=supplier_id, quantity_in_stock=stock)
    session.add(product)
    session.commit()
    print(f"Product '{name}' added successfully")
    session.close()

def list_products():
    session = Session()
    products = session.query(Product).all()
    data = [(p.id, p.name, p.quantity_in_stock, f"${p.price:.2f}", p.supplier.name) for p in products]
    print(tabulate(data, headers=["ID", "Name", "Stock", "Price", "Supplier"]))
    session.close()

def update_stock(product_id, quantity):
    session = Session()
    product = session.query(Product).get(product_id)
    if product:
        product.quantity_in_stock += quantity
        session.commit()
        print(f"Stock updated. New quantity: {product.quantity_in_stock}")
    else:
        print("Product not found")
    session.close()

def add_supplier(name, contact):
    session = Session()
    supplier = Supplier(name=name, contact_info=contact)
    session.add(supplier)
    session.commit()
    print(f"Supplier '{name}' added successfully")
    session.close()

def list_suppliers():
    session = Session()
    suppliers = session.query(Supplier).all()
    data = [(s.id, s.name, s.contact_info) for s in suppliers]
    print(tabulate(data, headers=["ID", "Name", "Contact"]))
    session.close()

def place_order(product_id, quantity):
    session = Session()
    product = session.query(Product).get(product_id)
    if product and product.quantity_in_stock >= quantity:
        order = Order(product_id=product_id, quantity=quantity)
        product.quantity_in_stock -= quantity
        session.add(order)
        session.commit()
        print(f"Order placed for {quantity} units of {product.name}")
    else:
        print("Insufficient stock or product not found")
    session.close()

def view_orders():
    session = Session()
    orders = session.query(Order).all()
    data = [(o.id, o.product.name, o.quantity, o.order_date.strftime("%Y-%m-%d")) for o in orders]
    print(tabulate(data, headers=["ID", "Product", "Quantity", "Date"]))
    session.close()

def main():
    init_db()
    parser = argparse.ArgumentParser(description="Inventory Manager CLI")
    subparsers = parser.add_subparsers(dest='command')
    
    # Add product
    add_prod = subparsers.add_parser('add-product')
    add_prod.add_argument('name')
    add_prod.add_argument('price', type=float)
    add_prod.add_argument('supplier_id', type=int)
    add_prod.add_argument('--stock', type=int, default=0)
    
    # List products
    subparsers.add_parser('list-products')
    
    # Update stock
    update = subparsers.add_parser('update-stock')
    update.add_argument('product_id', type=int)
    update.add_argument('quantity', type=int)
    
    # Add supplier
    add_sup = subparsers.add_parser('add-supplier')
    add_sup.add_argument('name')
    add_sup.add_argument('contact')
    
    # List suppliers
    subparsers.add_parser('list-suppliers')
    
    # Place order
    order = subparsers.add_parser('place-order')
    order.add_argument('product_id', type=int)
    order.add_argument('quantity', type=int)
    
    # View orders
    subparsers.add_parser('view-orders')
    
    args = parser.parse_args()
    
    if args.command == 'add-product':
        add_product(args.name, args.price, args.supplier_id, args.stock)
    elif args.command == 'list-products':
        list_products()
    elif args.command == 'update-stock':
        update_stock(args.product_id, args.quantity)
    elif args.command == 'add-supplier':
        add_supplier(args.name, args.contact)
    elif args.command == 'list-suppliers':
        list_suppliers()
    elif args.command == 'place-order':
        place_order(args.product_id, args.quantity)
    elif args.command == 'view-orders':
        view_orders()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()