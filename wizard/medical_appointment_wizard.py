# # -*- coding: utf-8 -*-
# # Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
# 
# from odoo import api, fields, models, _
# from datetime import date,datetime
# 
# class medical_appointment_wizard(models.TransientModel):
#     _name = "medical.appointment.wizard"
# 
#     speciality_id = fields.Many2one('medical.speciality','Speciality')
#     start_date = fields.Date("Start Date")
#     end_date = fields.Date('End Date')
# 
# # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: