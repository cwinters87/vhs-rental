# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


logger = logging.getLogger(__name__)


class VhsMovie(models.Model):
    _name = 'vhs.movie'
    _description = 'VHS movie'

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated', copy=False)
    director_ids = fields.Many2many('res.partner', string='Directors')
    category_id = fields.Many2one('vhs.movie.category', string='Category')
    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('lost', 'Lost')],
        'State', default="draft")

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                   ('available', 'rented'),
                   ('rented', 'available'),
                   ('available', 'lost'),
                   ('rented', 'lost'),
                   ('lost', 'available')]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for movie in self:
            if movie.is_allowed_transition(movie.state, new_state):
                movie.state = new_state
            else:
                message = _('Moving from %s to %s is not allowd') % (movie.state, new_state)
                raise UserError(message)

    def make_available(self):
        self.change_state('available')

    def make_rented(self):
        self.change_state('rented')

    def make_lost(self):
        self.change_state('lost')

    def create_categories(self):
        categ1 = {
            'name': 'Child category 1',
            'description': 'Description for child 1'
        }
        categ2 = {
            'name': 'Child category 2',
            'description': 'Description for child 2'
        }
        parent_category_val = {
            'name': 'Parent category',
            'email': 'Description for parent category',
            'child_ids': [
                (0, 0, categ1),
                (0, 0, categ2),
            ]
        }
        # Total 3 records (1 parent and 2 child) will be craeted in vhs.movie.category model
        record = self.env['vhs.movie.category'].create(parent_category_val)
        return True

    @api.multi
    def change_update_date(self):
        self.ensure_one()
        self.date_updated = fields.Datetime.now()

    @api.multi
    def find_movie(self):
        domain = [
            '|',
                '&', ('name', 'ilike', 'Movie Name'),
                     ('category_id.name', '=', 'Category Name'),
                '&', ('name', 'ilike', 'Movie Name 2'),
                     ('category_id.name', '=', 'Category Name 2')
        ]
        movies = self.search(domain)
        logger.info('Movies found: %s', movies)
        return True

    @api.model
    def get_all_vhs_members(self):
        vhs_member_model = self.env['vhs.member']  # This is an empty recordset of model vhs.member
        return vhs_member_model.search([])

    def filter_movies(self):
        all_movies = self.search([])
        filtered_movies = self.movies_with_multiple_directors(all_movies)
        logger.info('Filtered Movies: %s', filtered_movies)

    @api.model
    def movies_with_multiple_directors(self, all_movies):
        def predicate(movie):
            if len(movie.director_ids) > 1:
                return True
        return all_movies.filtered(predicate)

    def mapped_movies(self):
        all_movies = self.search([])
        movies_directors = self.get_director_names(all_movies)
        logger.info('Movies Director: %s', movies_directors)

    @api.model
    def get_director_names(self, all_movies):
        return all_movies.mapped('director_ids.name')


class VhsMember(models.Model):
    _name = 'vhs.member'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    date_start = fields.Date('Member Since')
    date_end = fields.Date('Termination Date')
    member_number = fields.Char()
    date_of_birth = fields.Date('Date of birth')