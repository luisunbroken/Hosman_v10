# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medicament_category(models.Model):
    _name = 'medicament.category'

    name = fields.Char(string="Category Name",required=True)
    parent_id = fields.Many2one('medicament.category',string='Parent Category')
