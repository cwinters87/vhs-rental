from typing_extensions import Required
from odoo import models, fields, api
from . import vhs

class Rental(models.Model):
    _name = 'rental'
    _description = 'VHS Rentals'
 
    name = fields.Many2one(
        'member', string='Member'
    )
    
    vhs_rental = fields.Many2many(
        'vhs.movie', domain=[('quantity', '>', 0)], string='VHS rented'
    )
    
    # vhs_rental = fields.Many2many(
    #     'vhs.movie', string='VHS rented', compute='_add'
    # )
    
    
    
    check_out_date = fields.Datetime(string="Checked Out", default=fields.Datetime.now, required=True)
    
    is_returned = fields.Boolean('Returned', default=False)
    
    rent_selected = fields.Boolean('Rent selected VHS', default=False, required=True)
    
    @api.onchange('rent_selected')
    def check_rented_true(self):
        if self.rent_selected == True:
            ids = []
            for rec in self:
                for item in rec.vhs_rental:
                    ids.append(item.id)
                    item.write({"quantity": item.quantity -1})
                    print(item.name)
                    print(item.quantity)
                # Credit to Eric for below code
                rec.vhs_rental= [(6, 0, ids)] 
                    
                    
# print(self.env['vhs.movie'].search([('id', '=', )]))
            
           
        
        
        
    # def _add(self):
    #     print("Hello from a function")
    
    
    
    # def add(self):
    #     self.vhs_rental.add_quantity()
    

    def _add(self):
        print("Hello from a function")
 
    
    # @api.depends('first_name', 'last_name')
    # def _get_name(self):
    #  for 