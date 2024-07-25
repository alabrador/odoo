{
    'name': 'Product Rental Management',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Manage product rentals with stock limit and reservation schedule',
    'description': """
    This module allows users to manage rentals of products, set stock limits, and allow customers to reserve products for specific dates and times.
    """,
    'author': 'GMX America',
    'depends': ['base', 'product', 'stock'],
    'data': [
        'security/rental_security.xml',
        'security/ir.model.access.csv',
        'views/rental_order_views.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
