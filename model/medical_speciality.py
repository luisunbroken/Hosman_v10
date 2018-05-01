# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_speciality(models.Model):
    _name="medical.speciality"

    name = fields.Char('Description',required=True)
    code = fields.Char('Code')

