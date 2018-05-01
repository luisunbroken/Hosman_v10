# # -*- coding: utf-8 -*-
# # Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
# 
# from odoo import api, fields, models, _
# from odoo.exceptions import UserError
# 
# class medical_paper_archive(models.Model):
#     _name = "medical.paper.archive"
# 
#     name = fields.Many2one('medical.patient',string="Patient ID", required=True)
#     identification_code = fields.Char('Code',default='PAC')
#     legacy = fields.Char('Legacy Code')
#     location = fields.Many2one('medical.hospital.unit','Unit', required=True)
#     hc_status = fields.Selection([
#             ('archived', 'Ambulatory'),
#             ('borrowed', 'Borrowed'),
#             ('lost', 'Lost'),
#         ], 'Status', sort=False, required=True)
#     current_location = fields.Many2one('medical.hospital.unit','Current Location', required=True)
#     requested_by = fields.Many2one('res.partner','Requested by', required=True)
#     request_date = fields.Datetime('Request Date')
#     return_date = fields.Datetime('Returned Date')
#     comments = fields.Text(string="comments")
# 
#     @api.model
#     def create(self, vals):
#         if vals.get('identification_code', 'PAC') == 'PAC':
#             vals['identification_code'] = self.env['ir.sequence'].next_by_code('medical.paper.archive') or 'PAC'
#         result = super(medical_paper_archive, self).create(vals)
# 
#         return result
# 
#     @api.onchange('name')
#     def onchange_patient_id(self):
#         patient_brw = self.env['medical.patient'].browse(self.name.id)
#         archive_name = patient_brw.patient_id.name
#         archive_obj = self.env['medical.paper.archive']
#         archive_ids = archive_obj.search([('name.patient_id.name','=',archive_name)])
#         if len(archive_ids) >= 1:
#             raise UserError(_('The Patient History already exists !'))
# 
# # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: