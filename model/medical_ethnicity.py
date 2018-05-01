# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_ethnicity(models.Model):
    _name="medical.ethnicity"

    name = fields.Char('Ethnic group',required=True)
    code = fields.Char('Code')
