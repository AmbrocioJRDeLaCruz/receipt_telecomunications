from odoo import fields, models, api

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    convertion = fields.Monetary(string="Conversion", compute="_get_convertion", readonly=True)
    price = fields.Float(string="Precio Dolar", compute="_get_convertion", readonly=True)
    
    @api.onchange('amount_total')
    def _get_convertion(self):
        if self.currency_id:
            for line in self.currency_id:
                records = line.rate_ids
                if records:
                    sorted_records = records.sorted(key=lambda r: r.id, reverse=True)
                    last_record = sorted_records[0]
                    desired_value = last_record.inverse_company_rate
                    self.convertion = self.amount_total * desired_value
                    self.price = desired_value
                    