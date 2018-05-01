# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_occupation(models.Model):
    _name="medical.occupation"

    name = fields.Char('Occupation',required=True)
    code = fields.Char('Code')
