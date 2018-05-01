# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_hospital_bed(models.Model):
    _name = 'medical.hospital.bed'
    _rec_name = 'hospital_bed_product_id'

    hospital_bed_product_id = fields.Many2one('product.product',string="Bed",required=True)
    bed_type = fields.Selection([('gatch','Gatch Bed'),('electric','Electric'),('stretcher','Stretcher'),('low_bed','Low Bed'),('low_air','Low Air Loss'),('c_electric','Circo Electric'),('clinitron','Clinitron')],required=True,string="Admission Type")
    state = fields.Selection([('occuiped','Occuiped'),('free','Free'),('reserved','Reserved'),('na','Not Available')],required=True,string="Status")
    extra_info = fields.Text(string="Extra Info")
    medical_hospital_ward_d = fields.Many2one('medical.hospital.ward',string="Ward")
    telephone_number = fields.Char(string="Telephone Number")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: