# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date

class medical_health_service(models.Model):
    _name = "medical.health_service"

    name = fields.Char('Name')
    is_invoiced = fields.Boolean(copy=False,default = False)
    description = fields.Char(string="Description", required=True)
    patient_id = fields.Many2one('medical.patient','Patient', required=True)
    service_date = fields.Date('Date')
    description = fields.Char('Description')
    service_line_ids = fields.One2many('medical.health_service.line','health_service_id','Service line')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('medical_health_ser') 
        result = super(medical_health_service, self).create(vals)
        return result

    @api.multi
    def button_set_to_confirm(self):
        self.write({'state':'confirmed'})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: