from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    dni = fields.Char(string='Nº DNI/NIE', require=True)
