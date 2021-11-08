from odoo import models, fields, api

class Rental(models.Model):
    _name = 'rental'
    _description = 'VHS Rentals'
 
    name = fields.Many2one(
        'member', string='Member'
    )
    
    vhs_rental = fields.Many2many(
        'vhs.movie', domain=[('quantity', '>', 0)], string='VHS rented'
    )
    
    check_out = fields.Datetime(string="Checked Out", default=fields.Datetime.now, required=True)
    
    is_returned = fields.Boolean('Returned', default=False)