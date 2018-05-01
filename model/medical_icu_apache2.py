# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime

class medical_icu_apache2(models.Model):
    _name = 'medical.icu.apache2'
    _rec_name = 'medical_inpatient_registration_id'

    medical_inpatient_registration_id = fields.Many2one('medical.inpatient.registration',string="Registration Code",required=True)
    score_date = fields.Datetime(string="Date",required=True)
    age = fields.Integer(string="Age")
    temperature = fields.Float(string="Temperature")
    heart_rate = fields.Float(string="Heart Rate")
    fio2 = fields.Float(string="Fio2")
    paco2 = fields.Float(string="PaCO2")
    ph = fields.Float(string="pH")
    serum_potassium = fields.Float(string="Potassium")
    hematocrit = fields.Float(string="Hematcocrit")
    arf = fields.Boolean(string="ARF")
    mean_ap = fields.Integer(string="MAP")
    respiratory_rate = fields.Integer(string='Respiratory Rate')
    pao2 = fields.Integer(string="PaO2")
    aado2 = fields.Integer(string="A-a DO2")
    serum_sodium = fields.Integer(string="Sodium")
    serum_creatinine = fields.Float(string="Creatinine")
    wbc = fields.Float(string="WBC")
    chronic_condition = fields.Boolean(string="Chronic Condition")
    apache_score = fields.Integer(string="Score")
    hospital_admission_type = fields.Selection([('me','Medical or emergency postoperative'),('el','elective postoperative')],string="Hospital Admission Type")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
