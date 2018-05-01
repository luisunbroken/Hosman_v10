# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_drug_form(models.Model):
    _name = 'medical.drug.form'

    name = fields.Char(string="Form",required=True)
    code = fields.Char(string="Code")

