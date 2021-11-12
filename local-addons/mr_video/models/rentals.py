from datetime import datetime, timedelta
from odoo import models, fields, api, exceptions

class Rental(models.Model):
    _name = 'rental'
    _description = 'VHS Rentals'
 
    name = fields.Many2one(
        'member', string='Member'
    )    
    vhs_rental = fields.Many2many(
        'vhs.movie', domain=[('quantity', '>', 0)], string='VHS rented'
    )       
    check_out_date = fields.Datetime(string="Checked Out", default=fields.Datetime.now, required=True)    
    return_date = fields.Datetime(compute='get_return_date')    
    rent_selected = fields.Boolean('Out for Rent', required=True)    
    is_due = fields.Boolean('Due', default=False)
    
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
        else:
            ids = []
            for rec in self:
                for item in rec.vhs_rental:
                    ids.append(item.id)
                    item.write({"quantity": item.quantity +1})
                    print(item.name)
                    print(item.quantity)
                # Credit to Eric for below code
                rec.vhs_rental= [(6, 0, ids)] 
                
    @api.depends('check_out_date')
    def get_return_date(self):
        for rec in self:
            rec.return_date = rec.check_out_date + timedelta(hours=48)
        
    @api.depends('return_date')
    def check_overdue(self):
        for rec in self:
            if datetime.now() > rec.return_date:
                rec.is_due = True
            else:
                rec.is_due = False
                
    @api.onchange('is_due')
    def check_bad_member(self):
        if self.is_due == True:
            for rec in self:
                for item in rec.name:
                    item.write({"is_bad_member": True})     
     
    @api.onchange('check_out_date')
    def overdue_check(self):
        self.check_overdue()
        
    @api.onchange('name')
    def verify_bad_member(self):
        for rec in self:
            if rec.env['member'].search([('id', '=', rec.name.id)]).is_bad_member:
                raise exceptions.Warning('{} is a bad member. Get good'.format(rec.name.name))