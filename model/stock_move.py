# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class stock_move(models.Model):
    _inherit = 'stock.move'
    
    medical_patient_rounding_move_id = fields.Many2one('medical.patient.ambulatory_care',string="Medical Patient Rounding")
    