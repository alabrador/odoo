from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_rental = fields.Boolean(string='Is a Rental Product')
    rental_stock = fields.Integer(string='Rental Stock', default=1)
