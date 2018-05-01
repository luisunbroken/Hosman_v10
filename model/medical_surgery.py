# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_surgery(models.Model):
    _name = "medical.surgery"
    _rec_name = 'procedure_id'

    procedure_id = fields.Many2one('medical.procedure',string='Code')
    patient_id = fields.Many2one('medical.patient',string="Patient")
    description = fields.Char('Description')
    pathology_id = fields.Many2one('medical.pathology','Base condition')
    classification = fields.Selection([
            ('o', 'Optional'),
            ('r', 'Required'),
            ('u', 'Urgent'),
            ('e', 'Emergency'),
        ], 'Surgery Classification', sort=False)
    date = fields.Datetime('Date of the surgery')
    age = fields.Char('Patient Age')
    surgeon_id = fields.Many2one('medical.physician','Surgeon')
    anesthetist_physician_id = fields.Many2one('medical.physician','Anesthetist')
    operating_room_id = fields.Many2one('medical.hospital.oprating.room','Operating Room')
    surgery_end_date = fields.Datetime('End of the surgery')
    surgery_length = fields.Char('Duration')
    signed_by_physician_id = fields.Many2one('medical.physician','Signed by')
    preop_bleeding_risk = fields.Boolean('Risk of Massive bleeding')
    preop_oximeter = fields.Boolean('Pulse Oximeter in place')
    preop_site_marking = fields.Boolean('Surgical Site Marking')
    preop_antibiotics = fields.Boolean('Antibiotic Prophylaxis')
    preop_sterility = fields.Boolean('Sterility confirmed')
    preop_mallampati = fields.Selection([
            ('class 1', 'Class 1: Full visibility of tonsils, uvula and soft palate'),
            ('class 2', 'Class 2: Visibility of hard and soft palate, upper portion of tonsils and uvula'),
            ('class 3', 'Class 3: Soft and hard palate and base of the uvula are visible'),
            ('class 4', 'Class 4: Only hard palate visible'),
        ], 'Mallampati Score', sort=False)
    rcri_id = fields.Many2one('medical.rcri','RCRI')
    preop_asa = fields.Selection([
            ('ps1', 'PS 1: Normal healthy patient'),
            ('ps2', 'PS 2: Patients with mild systemic disease'),
            ('ps3', 'PS 3: Patients with severe systemic disease'),
            ('ps4', 'PS 4: Patients with severe systemic disease that is a constant threat to life'),
            ('ps5', 'PS 5: Moribund patients who are not expected to survive without the operation'),
            ('ps6', 'PS 6: A declared brain-dead patient who organs are being removed for donor purposes'),
        ], 'ASA PS', sort=False)
    operation_ids = fields.One2many('medical.operation','medical_surgery_id')
    extra_info = fields.Text(string="Extra Info")
    anesthesia_report = fields.Text(string="Anesthesia Report")

    @api.onchange('date','surgery_end_date')
    def onchange_duration(self):
        if self.date and self.surgery_end_date:
            dt1 = self.date
            dt2 = self.surgery_end_date
            d1 = datetime.strptime(dt1, "%Y-%m-%d %H:%M:%S")
            d2 = datetime.strptime(dt2, "%Y-%m-%d %H:%M:%S")
            rd = d2-d1
            houser=rd // 3600
            val=str((rd.seconds//3600)%3600)
            self.surgery_length = str(rd.seconds//3600) +'' + 'h'+' ' + str((rd.seconds//60)%60) +''+ 'm'

    @api.multi
    def done(self):
        self.write({'state':'done'})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
