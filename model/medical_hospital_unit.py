# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_hospital_unit(models.Model):
    _name = 'medical.hospital.unit'

    name = fields.Char(string="Name",required=True)
    code = fields.Char(string="Code")
    extra_info = fields.Text(string="Extra Info")
    medical_hospital_unit_institution_id = fields.Many2one('res.partner',domain=[('is_institution','=',True)],string="Institution")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
