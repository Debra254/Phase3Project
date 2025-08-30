https://drive.google.com/file/d/1Fr2ADPWoM_1Z0uD9NZHjXQqXqEUhQiZG/view?usp=sharing

# Inventory Manager CLI

A command-line application to manage products, suppliers, and orders.

## Setup

```bash
pipenv install
pipenv shell
```

## Usage

```bash
# Show help
python inventory_manager/cli.py --help

# Add suppliers
python inventory_manager/cli.py add-supplier "ABC Corp" "contact@abc.com"

# List suppliers
python inventory_manager/cli.py list-suppliers

# Add products
python inventory_manager/cli.py add-product "Laptop" 999.99 1 --stock 10

# List products
python inventory_manager/cli.py list-products

# Update stock
python inventory_manager/cli.py update-stock 1 5

# Place order
python inventory_manager/cli.py place-order 1 2

# View orders
python inventory_manager/cli.py view-orders

# Add sample data
python inventory_manager/seed.py
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
