# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime
from odoo.exceptions import UserError

class medical_bed_transfer_wizard(models.TransientModel):
    _name = "medical.bed.transfer.wizard"
    _recname = 'medical_hospital_bed_id'

    medical_hospital_bed_id = fields.Many2one('medical.hospital.bed',string="New Bed",required=True )
    reason = fields.Char('Reason',required=True)

    @api.multi
    def bed_transfer(self):
        record = self
        medic_imp_obj = self.env['medical.inpatient.registration']
        medic_imp_rec= medic_imp_obj.browse(self._context.get('active_id'))
        if medic_imp_rec.state == 'hospitalized':
            if record.medical_hospital_bed_id.state == 'free':
               record.medical_hospital_bed_id.state = 'occuiped'
               medic_imp_rec.write({'medical_hospital_bed_id':record.medical_hospital_bed_id.id,'bed_transfers_ids': [(0,0,{'date': date.today(),
                                                             'bed_to':record.medical_hospital_bed_id.id,
                                                              'bed_from':medic_imp_rec.medical_hospital_bed_id.id,
                                                              'inpatient_id':medic_imp_rec.patient_id.id,
                                                              'reason':record.reason})] })
               medic_imp_rec.medical_hospital_bed_id = record.medical_hospital_bed_id.id
            else:
                raise UserError("Bed is occupied")
        else:
           raise UserError("Bed transfer is only allowed in hospitalize stage")
#         res = self.env['bed.transfer'].create({'date': date.today(),
#                                                              'bed_to':record.medical_hospital_bed_id.id,
#                                                               'bed_from':medic_imp_rec.medical_hospital_bed_id.id,
#                                                               'inpatient_id':medic_imp_rec.patient_id.id,
#                                                               'reason':record.reason})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
