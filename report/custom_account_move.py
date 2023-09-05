# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details

from odoo import api, fields, models 

class AccountTelecomunicationsReceipt(models.AbstractModel):
    _name = 'account.telecomunications.receipt'
    _description = 'Receipt Informatica & Telecomunicaciones de contabilidad'
    
    @api.model
    def _get_report_account_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'account.move',
            'docs': docs,
            'proforma': True,
        }