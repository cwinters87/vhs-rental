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

    # def book_rent(self):
    #     self.ensure_one()
    #     if self.state != 'available':
    #         raise UserError(_('VHS is not available for renting'))
    #     rent_as_superuser = self.env['library.book.rent'].sudo()
    #     rent_as_superuser.create({
    #         'book_id': self.id,
    #         'borrower_id': self.env.user.partner_id.id,
    #     })
    

    # @api.model
    # def is_allowed_transition(self, old_state, new_state):
    #     allowed = [('draft', 'available'),
    #                ('available', 'rented'),
    #                ('rented', 'available'),
    #                ('available', 'lost'),
    #                ('rented', 'lost'),
    #                ('lost', 'available')]
    #     return (old_state, new_state) in allowed

    # @api.multi
    # def change_state(self, new_state):
    #     for movie in self:
    #         if movie.is_allowed_transition(movie.state, new_state):
    #             movie.state = new_state
    #         else:
    #             message = _('Moving from %s to %s is not allowd') % (movie.state, new_state)
    #             raise UserError(message)

    # def make_available(self):
    #     self.change_state('available')

    # def make_rented(self):
    #     self.change_state('rented')

    # def make_lost(self):
    #     self.change_state('lost')

    # def create_genres(self):
    #     categ1 = {
    #         'name': 'Child genre 1',
    #         'description': 'Description for child 1'
    #     }
    #     categ2 = {
    #         'name': 'Child genre 2',
    #         'description': 'Description for child 2'
    #     }
    #     parent_genre_val = {
    #         'name': 'Parent genre',
    #         'email': 'Description for parent genre',
    #         'child_ids': [
    #             (0, 0, categ1),
    #             (0, 0, categ2),
    #         ]
    #     }
        # Total 3 records (1 parent and 2 child) will be craeted in vhs.movie.genre model
        # record = self.env['vhs.movie.genre'].create(parent_genre_val)
        # return True

    # @api.multi
    # def change_update_date(self):
    #     self.ensure_one()
    #     self.date_updated = fields.Datetime.now()

    # @api.multi
    # def find_movie(self):
    #     domain = [
    #         '|',
    #             '&', ('name', 'ilike', 'Movie Name'),
    #                  ('genre_id.name', '=', 'Genre Name'),
    #             '&', ('name', 'ilike', 'Movie Name 2'),
    #                  ('genre_id.name', '=', 'Genre Name 2')
    #     ]
    #     movies = self.search(domain)
    #     logger.info('Movies found: %s', movies)
    #     return True

    # @api.model
    # def get_all_vhs_members(self):
    #     vhs_member_model = self.env['vhs.member']  # This is an empty recordset of model vhs.member
    #     return vhs_member_model.search([])

    # def filter_movies(self):
    #     all_movies = self.search([])
    #     filtered_movies = self.movies_with_multiple_directors(all_movies)
    #     logger.info('Filtered Movies: %s', filtered_movies)

    # @api.model
    # def movies_with_multiple_directors(self, all_movies):
    #     def predicate(movie):
    #         if len(movie.director) > 1:
    #             return True
    #     return all_movies.filtered(predicate)

    # def mapped_movies(self):
    #     all_movies = self.search([])
    #     movies_directors = self.get_director_names(all_movies)
    #     logger.info('Movies Director: %s', movies_directors)

    # @api.model
    # def get_director_names(self, all_movies):
    #     return all_movies.mapped('director_ids.name')


# class VhsMember(models.Model):
#     _name = 'vhs.member'
#     _inherits = {'res.partner': 'partner_id'}

#     partner_id = fields.Many2one('res.partner', ondelete='cascade')
#     date_start = fields.Date('Member Since')
#     date_end = fields.Date('Termination Date')
#     member_number = fields.Char()
#     date_of_birth = fields.Date('Date of birth')


# class Rental(models.Model):
#     _name = 'rental'
#     _description = 'VHS Rentals'
 
#     name = fields.Many2one(
#         'member', string='Member'
#     )
    
#     vhs_rental = fields.Many2many(
#         'vhs.movie', domain=[('quantity', '>', 0)], string='VHS rented'
#     )
    
#     check_out = fields.Datetime(string="Checked Out", default=fields.Datetime.now, required=True)
    
#     is_returned = fields.Boolean('Returned', default=False)
    
#     def add(self):
#         return VhsMovie.add_quantity



def my_function():
  print("Hello from a function")

my_function()