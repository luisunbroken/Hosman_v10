# # -*- coding: utf-8 -*-
# # Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
# 
# from odoo import api, fields, models, _
# 
# class medical_imaging_test_request_wizard(models.TransientModel):
#     _name = "medical.imaging.test.request.wizard"
# 
#     phy_id = fields.Many2one('medical.physician',string="Name Of Physician", required = True)
#     patient_id = fields.Many2one('medical.patient',string="Patient", required = True)
#     test_date = fields.Date('Test Date', required = True)
#     urgent = fields.Boolean('Urgent')
#     test_ids = fields.Many2many('medical.imaging.test','img_test_report_test_rel', 'test_id', 'imag_id','Test')
# 
# 
#     @api.multi
#     def create_lab_imaging_request(self):
#         for wizard_obj in self:
#             patient_id = wizard_obj.patient_id
#             phy_id = wizard_obj.phy_id
#             urgent = wizard_obj.urgent
#             new_created_id_list  = []
#             date = wizard_obj.test_date
#             for test_id in wizard_obj.test_ids:
#                 imag_test_req_obj = self.env['medical.imaging.test.request']
#                 new_created_id = imag_test_req_obj.create({'test_date': date,
#                                                             'request_id': phy_id.id,
#                                                             'physician_id':phy_id.id,
#                                                             'patient_id':patient_id.id,
#                                                             'state': 'draft',
#                                                             'urgent':urgent,
#                                                             'test_id':test_id.id,
#                                                             'name':self.env['ir.sequence'].next_by_code('imaging_seq')
#           })
#     
#     
#                 new_created_id_list.append(new_created_id.id)
#             if new_created_id_list:
#                 imd = self.env['ir.model.data']
#                 action = imd.xmlid_to_object('hospital_management.action_medical_imaging_test_result_draft')
#                 list_view_id = imd.xmlid_to_res_id('hospital_management.medical_imaging_test_request_tree')
#     
#                 result = {
#                                     'name': action.name,
#                                     'help': action.help,
#                                     'type': action.type,
#                                     'views': [ [list_view_id,'tree' ]],
#                                     'target': action.target,
#                                     'context': action.context,
#                                     'res_model': action.res_model,
#                                 }
#                 if len(new_created_id_list)  :
#                             result['domain'] = "[('id','in',%s)]" % new_created_id_list
#                 return result
# 
# 
# # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: