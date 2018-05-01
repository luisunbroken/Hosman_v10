# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_ambulatory_care_procedure(models.Model):
    _name = 'medical.ambulatory_care_procedure'
    _rec_name = 'procedure_id'

    procedure_id = fields.Many2one('medical.procedure',string="Code",required=True)   
    comments = fields.Char(string="Comments") 
    medical_patient_ambulatory_care_procedure_id = fields.Many2one('medical.patient.ambulatory_care',string="Procedure")

