# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
 
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date,datetime

class medical_inpatient_icu(models.Model):
    _name = 'medical.inpatient.icu'
    _rec_name ='medical_inpatient_registration_id'

    medical_inpatient_registration_id = fields.Many2one('medical.inpatient.registration',string="Registration Code",required=True)
    admitted =fields.Boolean(string="Admitted",required=True,default=True)
    icu_admission_date = fields.Datetime(string="ICU Admission",required=True)
    icu_stay = fields.Char(string="Duration",required=True,size=128)
    discharged_from_icu =fields.Boolean(string="Discharged")
    icu_discharge_date  = fields.Datetime(string='Discharge')
    medical_icu_ventilation_ids = fields.One2many('medical.icu.ventilation','medical_inpatient_icu_id',string='MV History')

    @api.onchange('medical_inpatient_registration_id')
    @api.multi
    def onchange_patient(self):
        for each in self:
            inpatient_icu_obj = each.env['medical.inpatient.icu']
            inpatient_icu_ids = inpatient_icu_obj.search([('medical_inpatient_registration_id.name','=',each.medical_inpatient_registration_id.name)])
            print inpatient_icu_ids
            if len(inpatient_icu_ids) > 1:
                raise UserError(_('Our records indicate that the patient is already admitted at ICU. '))

    @api.onchange('admitted','discharged_from_icu')
    @api.multi
    def onchange_with_descharge(self):
        for each in self:
            if each.discharged_from_icu == True:
                each.admitted = False
            else:
                each.admitted = True
 
    @api.onchange('admitted','discharged_from_icu')
    @api.multi
    def onchange_with_admitted(self):
        for each in self:
            if each.admitted == True:
                each.discharged_from_icu = False
            else:
                each.discharged_from_icu = True


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
