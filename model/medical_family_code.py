# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_family_code(models.Model):
    _name = "medical.family_code"

    name = fields.Char(string="Name", required=True)
    operational_sector_id = fields.Many2one('medical.operational_sector', string="Operational Sector")
    members_ids = fields.Many2many('res.partner',string="Members")
    info = fields.Text(string="Extra info")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: