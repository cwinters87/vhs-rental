# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MovieGenre(models.Model):
    _name = 'vhs.movie.genre'

    _parent_store = True
    _parent_name = "parent_id"  # optional if field is 'parent_id'

    name = fields.Char('Genre')
    description = fields.Text('Description')
    parent_id = fields.Many2one(
        'vhs.movie.genre',
        string='Parent Genre',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'vhs.movie.genre', 'parent_id',
        string='Child Genres')
    parent_path = fields.Char(index=True)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive genres.')