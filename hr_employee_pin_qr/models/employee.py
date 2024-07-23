from odoo import fields, models, api
import qrcode
import base64
from io import BytesIO

class Employee(models.Model):
    _inherit = 'hr.employee'
    
    qr_code = fields.Binary("QR Code", attachment=True, readonly=True)

    @api.depends('pin')

    def generate_qr_code(self):
        for employee in self:
            if employee.pin:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(employee.pin)
                qr.make(fit=True)

                img = qr.make_image(fill='black', back_color='white')
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                qr_image = base64.b64encode(buffer.getvalue())
                employee.pin = qr_image
            else:
                employee.pin = False