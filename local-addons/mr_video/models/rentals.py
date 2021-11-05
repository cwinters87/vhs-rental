from odoo import models, fields, api

class Rental(models.Model):
    _name = 'rental'
    _description = 'VHS Rentals'
    
    renter = fields.Many2one(
        'member', string='Member'
    )
    
    vhs_rental = fields.Many2many(
        'vhs.movie', domain=[('quantity', '>', 0)], string='VHS to rent'
    )
    