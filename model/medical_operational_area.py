# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_operational_area(models.Model):
    _name = 'medical.operational_area'
    
    name = fields.Char(string="Name",required=True)
    info = fields.Text(string="Extra Info")
    operational_sector_ids = fields.One2many('medical.operational_sector','operational_area_id',string="Operational sector")

