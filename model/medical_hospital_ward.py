# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_hospital_ward(models.Model):
    _name = 'medical.hospital.ward'

    name = fields.Char(string="Name",required=True)
    medical_hospital_ward_institution_id = fields.Many2one('res.partner',domain=[('is_institution','=',True)],string="Institution")
    medical_hospital_building_id = fields.Many2one('medical.hospital.building',string="Building")
    floor = fields.Integer(string="Floor Number")
    medical_hospital_unit_id = fields.Many2one('medical.hospital.unit',string="Unit")
    gender = fields.Selection([('men','Men Ward'),('women','Women Ward'),('unisex','Unisex')],string="Gender",required=True)
    private = fields.Boolean(string="Private")
    bio_hazard = fields.Boolean(string="Bio Hazard")
    number_of_beds = fields.Integer(string="Number Of Beds")
    telephone = fields.Boolean(string="Telephone Access")
    private_bathroom = fields.Boolean(string="Private Bathroom")
    tv = fields.Boolean(string="Television")
    ac = fields.Boolean(string="Air Conditioning")
    guest_sofa = fields.Boolean(string="Guest Sofa Bed")
    internet = fields.Boolean(string="Internet Access")
    microwave = fields.Boolean(string="Microwave")
    refrigerator = fields.Boolean(string="Refrigetator")
    state = fields.Selection([('beds_available','Beds Available'),('full','Full'),('na','Not Available')],string="Status")
    extra_info = fields.Text(string="Extra Info")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
