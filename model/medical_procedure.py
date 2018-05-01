# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_procedure(models.Model):
    _name = 'medical.procedure'

    name = fields.Char(string='Code',required=True)
    description = fields.Text(string='Long Text')

