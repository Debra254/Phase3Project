from setuptools import setup, find_packages

setup(
    name="inventory-manager",
    version="1.0.0",
    py_modules=['cli', 'models'],
    entry_points={
        'console_scripts': [
            'inventory=cli:main',
        ],
    },
)