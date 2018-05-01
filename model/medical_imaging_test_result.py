# # -*- coding: utf-8 -*-
# # Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
# 
# from odoo import models, fields, api, _
# from datetime import date,datetime
# 
# class medical_imaging_test_result(models.Model):
#     _name = 'medical.imaging.test.result'
# 
#     name = fields.Char(string="Name",default='IMGR')
#     test_date = fields.Datetime(string="Date", default = fields.Date.context_today)
#     request_id = fields.Many2one('medical.imaging.test.request',string="Test request", readonly=True)
#     request_date = fields.Datetime(string="Request Date", readonly=True)
#     test_id = fields.Many2one('medical.imaging.test','Test', readonly=True)
#     patient_id = fields.Many2one('medical.patient','Patient', readonly=True)
#     physician_id = fields.Many2one('medical.physician','Physician', required = True)
#     images_ids = fields.One2many('ir.attachment','imaging_result_id','Images')
#     comments = fields.Text(string="Comments")
# 
# 
#     @api.model
#     def create(self, vals):
#         if vals.get('name', 'IMGR') == 'IMGR':
#             vals['name'] = self.env['ir.sequence'].next_by_code('medical.imaging.test.result') or 'IMGR'
#         result = super(medical_imaging_test_result, self).create(vals)
#         return result

