from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    dni = fields.Char(string='DNI/NIE', require=True)
