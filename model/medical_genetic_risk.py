# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_genetic_risk(models.Model):
    _name = 'medical.genetic.risk'
    _rec_name = 'long_name'

    name = fields.Char(string="Name")
    chromosome = fields.Char(string="Affected Chromosome",help="Name of the affected chromosome")
    location = fields.Char(string="Location",help="Locus of the chromosome")
    info = fields.Text(string="Information",help="Name of the protein(s) affected")
    long_name = fields.Char(string="Official Long Name",reuiqred=True)
    dominance = fields.Selection([('dominant','Dominant'),('recessive','Recessive')],string="Dominance")
    gene = fields.Char(string="Gene ID",help="default code from NCBI Entrez database.")

