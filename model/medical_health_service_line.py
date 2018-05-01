# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
 
from odoo import api, fields, models, _
from datetime import date
 
class medical_health_service_line(models.Model):
    _name = "medical.health_service.line"
    _rec_name = 'health_service_id'

    health_service_id = fields.Many2one('medical.health_service')
    to_invoice = fields.Boolean('Invoice', default =True)
    description = fields.Char('Description')
    product_id = fields.Many2one('product.product','Product')
    qty = fields.Integer('Qty')
    from_date = fields.Date('From')
    to_date = fields.Date('To')
 
 
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: