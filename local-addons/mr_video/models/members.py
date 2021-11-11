# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
from odoo.tools.translate import _

logger = logging.getLogger(__name__)

class Member(models.Model):
    _name = 'member'
    _description = 'Mr Video Member'
    
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    phone_number = fields.Char('Phone Number', required=True)
    email = fields.Char('Email Address')    
    name = fields.Char(
        string='Name',
        compute='_get_name'
    )    
    history = fields.One2many('rental', string='Rental Records', compute='get_history', readonly=True)
    is_bad_member = fields.Boolean('Bad Member', default=False)
        
    @api.depends('first_name', 'last_name')
    def _get_name(self):
     for rec in self:
         rec.name = '{first} {last}'.format(first=rec.first_name, last=rec.last_name)    
    
    @api.multi
    def get_history(self):
        ids = []
        for rec in self:
            history_records = rec.env['rental'].search([('name', '=', rec.name)])
            for recs in history_records:
                ids.append(recs.id)
                
        rec.history = [(6, 0, ids)]