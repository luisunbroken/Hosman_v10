# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_ambulatory_care(models.Model):
    _name = 'medical.patient.ambulatory_care'

    name = fields.Char(string='Name',required=True,size=256)
    ordering_physician_id = fields.Many2one('medical.physician',string='Ordering Physician')
    base_condition_pathology_id = fields.Many2one('medical.pathology',string='Base Condition')
    session_number = fields.Integer(string = 'Session #',required=True)
    health_physician_id = fields.Many2one('medical.physician',string='Health Professional')
    patient_id = fields.Many2one('medical.patient',string='Patient',required=True)
    medical_patient_evaluation_id = fields.Many2one('medical.patient.evaluation',string='Related Evaluation')
    session_start = fields.Datetime(string='Start',required=True)
    state = fields.Selection([('done','Done'),
                              ('draft','Draft')],
                             string='Status')
    procedures_ids = fields.One2many('medical.ambulatory_care_procedure','medical_patient_ambulatory_care_procedure_id')
    session_notes = fields.Text(string='Session',required=True,default='Stable')
    warning = fields.Boolean(string='Warning')
    session_end = fields.Datetime(string="End",required=True)
    next_session = fields.Datetime(string='Next Session')
    temperature =fields.Float(string='Temperature')
    systolic = fields.Integer(string="Systolic Pressure")
    diastolic = fields.Integer(string='Diastolic Pressure')
    bpm = fields.Integer(string='Heart Rate')
    respiratory_rate = fields.Integer(string="Respiratory Rate")
    osat = fields.Integer(string="Oxygen Saturation")
    glycemia = fields.Integer(string="Glycemia")
    evolution = fields.Selection([('initial','Initial'),
                                  ('n','Status Quo'),
                                  ('i','Improving'),
                                  ('w','Worsening')],
                                 string="Evolution")
    stock_location_id = fields.Many2one('stock.location',string='Care Location')
    medicaments_ids = fields.One2many('medical.patient.ambulatory_care.medicament','medical_patient_rounding_ambulatory_care_medicament_id',string='Medicaments')
    medical_supplies_ids = fields.One2many('medical.patient.ambulatory_care.medical_supply','medical_patient_rounding_ambulatory_care_supply_id',string='Medical Supplier')
    vaccines_ids = fields.One2many('medical.patient.ambulatory_care.vaccine','medical_patient_ambulatory_care_vaccine_id',string='Vaccines')
    move_ids = fields.One2many('stock.move','medical_patient_rounding_move_id',string="Moves")

