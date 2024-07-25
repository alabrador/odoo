from odoo import models, fields, api
from datetime import timedelta

class RentalOrder(models.Model):
    _name = 'rental.order'
    _description = 'Rental Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: 'New')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    rental_date_start = fields.Datetime(string='Rental Start Date', required=True)
    rental_date_end = fields.Datetime(string='Rental End Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', readonly=True, index=True, default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('rental.order') or 'New'
        result = super(RentalOrder, self).create(vals)
        return result

    @api.constrains('product_id', 'rental_date_start', 'rental_date_end')
    def _check_availability(self):
        for order in self:
            overlapping_orders = self.env['rental.order'].search([
                ('product_id', '=', order.product_id.id),
                ('state', 'in', ['confirmed', 'done']),
                ('rental_date_start', '<', order.rental_date_end),
                ('rental_date_end', '>', order.rental_date_start),
                ('id', '!=', order.id),
            ])
            if overlapping_orders:
                raise ValidationError('The product is already rented for the selected period.')

    def action_confirm(self):
        for order in self:
            order.state = 'confirmed'

    def action_cancel(self):
        for order in self:
            order.state = 'cancelled'

    def action_done(self):
        for order in self:
            order.state = 'done'
