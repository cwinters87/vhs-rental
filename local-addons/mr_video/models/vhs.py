# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.date_utils import subtract
from odoo.tools.translate import _

logger = logging.getLogger(__name__)

class VhsMovie(models.Model):
    _name = 'vhs.movie'
    _description = 'Mr Video VHS Movies'   
    
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')    
    director = fields.Char('Director')
    genre = fields.Char('Genre')
    poster =fields.Binary(string='Movie Poster')
    quantity = fields.Integer('Amount in Stock', required=True)    
    state = fields.Selection(
        [('available', 'Available'),
         ('rented', 'Rented')],
        'State', default="available")
    
    def make_available(self):
        self.ensure_one()
        self.state = 'available'

    def make_rented(self):
        self.ensure_one()
        self.state = 'rented'
           
    def add_quantity(self):
        added_quantity = self.quantity + 1
        return added_quantity

    def subtrat_quantity(self):
        subtracted_quantity = self.quantity - 1
        return subtracted_quantity