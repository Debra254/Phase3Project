from setuptools import setup, find_packages

setup(
    name="inventory-manager",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'inventory=inventory_manager.cli:main',
        ],
    },
)