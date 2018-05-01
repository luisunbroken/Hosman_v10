# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_newborn(models.Model):
    _name = 'medical.newborn'

    name = fields.Char('Name', readonly = True)
    mother_patient_id = fields.Many2one('medical.patient','Mother',required=True, domain="[('sex', '=', 'f')]")
    birth_date  = fields.Date('Date of Birth' , required = True)
    length = fields.Integer('Length', )
    cephalic_perimeter = fields.Integer('Cephalic Perimeter')
    baby_name  = fields.Char('Baby\'s name')
    sex  = fields.Selection([('m','Male'), ('f','Female'),('a','Ambiguous Genitalia ')], required = True ) 
    dismissed  = fields.Datetime('Discharged')
    weight = fields.Integer('Weight')
    responsible_physician_id = fields.Many2one('medical.physician','Doctor in charge')
    photo = fields.Binary('Picture')
    meconium = fields.Boolean('Meconium')
    neonatal_ambiguous_genitalia = fields.Boolean('Ambiguous Genitalia')
    neonatal_babinski_reflex = fields.Boolean('Babinski Reflex')
    neonatal_barlow = fields.Boolean('Positive Barlow')
    neonatal_blink_reflex = fields.Boolean('Blink Reflex')
    neonatal_erbs_palsy = fields.Boolean('Erbs Palsy')
    neonatal_grasp_reflex =fields.Boolean('Grasp Reflex')
    neonatal_hematoma = fields.Boolean('Hematomas')
    neonatal_hernia = fields.Boolean('Hernia')
    neonatal_moro_reflex = fields.Boolean('Moro Reflex')
    neonatal_ortolani = fields.Boolean('Positive Ortolani')
    neonatal_palmar_crease = fields.Boolean('Transversal Palmar Crease')
    neonatal_polydactyly = fields.Boolean('Polydactyly')
    neonatal_rooting_reflex = fields.Boolean('Rooting Reflex')
    neonatal_stepping_reflex = fields.Boolean('Stepping Reflex')
    neonatal_sucking_reflex = fields.Boolean('Sucking Reflex')
    neonatal_swimming_reflex = fields.Boolean('Swimming Reflex')
    neonatal_syndactyly = fields.Boolean('Syndactyly')
    neonatal_talipes_equinovarus = fields.Boolean('Talipes Equinovarus')
    neonatal_tonic_neck_reflex = fields.Boolean('Tonic Neck Reflex')
    died_at_delivery = fields.Boolean('Died at delivery room')
    died_being_transferred = fields.Boolean('Died at Transfered')
    died_at_the_hospital = fields.Boolean('Died at the hospital')

    reanimation_aspiration = fields.Boolean('Aspiration')
    reanimation_intubation = fields.Boolean('Intubation')
    reanimation_mask = fields.Boolean('Mask')
    reanimation_oxygen = fields.Boolean('Oxygen')
    reanimation_stimulation = fields.Boolean('Stimulation')
    test_audition = fields.Boolean('Audition')
    test_billirubin = fields.Boolean('Billirubin')
    test_chagas = fields.Boolean('Chagas')
    test_metabolic = fields.Boolean('Metabolic ("heel stick screening")')
    test_toxo = fields.Boolean('Toxoplasmosis')
    test_vdrl = fields.Boolean('VDRL')
    still_birth = fields.Boolean('Stillbirth')
    time_of_death = fields.Datetime('Time of Death')
    notes = fields.Text('Notes')
    cause_of_death = fields.Many2one('medical.pathology','Cause Of Death')
    congenital_disease_ids = fields.One2many('medical.patient.disease', 'new_born_id')
    medication_ids = fields.One2many('medical.patient.medication1', 'new_born_id')
    apgar_score_ids = fields.One2many('medical.neomatal.apgar', 'new_born_id')

    @api.model
    def create(self,val):
        val['name'] = self.env['ir.sequence'].next_by_code('new_born_seq')
        result = super(medical_newborn, self).create(val)
        return result

    @api.multi
    def print_card(self):
        return self.env['report'].get_action(self, 'hospital_management.report_newborn_card')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    