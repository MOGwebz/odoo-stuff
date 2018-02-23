from odoo import fields,models

class TaxInvoice(models.Model):
    _inherit = 'account.invoice'
    tax_invoice = fields.Boolean()