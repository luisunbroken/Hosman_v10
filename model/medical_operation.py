# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_operation(models.Model):
    _name = 'medical.operation'

    medical_procedure_id = fields.Many2one('medical.procedure',string='Code')
    notes = fields.Text(string='Notes')
    medical_surgery_id = fields.Many2one('medical.surgery','Surgery')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
