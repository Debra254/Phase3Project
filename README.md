# Inventory Manager CLI

A command-line application to manage products, suppliers, and orders.

## Setup

```bash
pipenv install
pipenv shell
```

## Usage

```bash
# Add a supplier
python cli.py add-supplier "ABC Corp" "contact@abc.com"

# Add a product
python cli.py add-product "Laptop" 999.99 1 --stock 10

# List products
python cli.py list-products

# Update stock
python cli.py update-stock 1 5

# Place order
python cli.py place-order 1 2

# View orders
python cli.py view-orders

# List suppliers
python cli.py list-suppliers
```

## Database Schema

- **Suppliers**: id, name, contact_info
- **Products**: id, name, quantity_in_stock, price, supplier_id (FK)
- **Orders**: id, product_id (FK), quantity, order_date

## Features

- SQLAlchemy ORM with 3 related tables
- CLI with argparse
- Virtual environment with Pipenv
- Uses lists, dicts, and tuples for data handling