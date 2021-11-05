# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


logger = logging.getLogger(__name__)

class Member(models.Model):
    _name = 'member'
    _description = 'VHS movie'
    
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    phone_number = fields.Char('Phone Number', required=True)
    email = fields.Char('Email Address')
    
    @api.model
    def get_all_members(self):
        member_model = self.env['member']  # This is an empty recordset of model vhs.member
        return member_model.search([])
    
    

    # partner_id = fields.Many2one('res.partner', ondelete='cascade')
    # date_start = fields.Date('Member Since')
    # date_end = fields.Date('Termination Date')
    # member_number = fields.Char()
    # date_of_birth = fields.Date('Date of birth')