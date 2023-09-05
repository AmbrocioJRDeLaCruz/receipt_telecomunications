from odoo import api, fields, models

class SalesTelecomunicationsReceipt(models.AbstractModel):
    _name = 'sale.telecomunications.receipt'
    _description = 'Receipt Informatica & Telecomunicaciones de venta'

    @api.model
    def _get_report_sales_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'sale.order',
            'docs': docs,
            'proforma': True
        }
