# employee_qr_code/__manifest__.py
{
    'name': 'Employee QR Code',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Generate QR code based on employee PIN',
    'description': 'This module generates a QR code based on the employee PIN for identification purposes.',
    'author': 'GMX America',
    'website': 'https://gmxamerica.com',
    'contributors': [
        'Alexander Labrador <alabrador@gmxamerica.com>',
    ],
    'license': 'GPL-3',
    'depends': ['base', 'hr'],
    'data': [
        'views/view_pin_qr.xml',
    ],
    'images': [
        'static/description/icon.png'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}