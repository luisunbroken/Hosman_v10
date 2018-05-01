# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_hospital_oprating_room(models.Model):
    _name = 'medical.hospital.oprating.room'

    name = fields.Char(string="Name",required=True,size=128)
    medical_hospital_building_id = fields.Many2one('medical.hospital.building',string="Building")
    extra_info = fields.Text(string="Extra Info")
    institution_partner_id = fields.Many2one('res.partner',domain=[('is_institution','=',True)],string="Institution")
    medical_hospital_unit_id = fields.Many2one('medical.hospital.unit',string="Unit")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s