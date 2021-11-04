# -*- coding: utf-8 -*-
from odoo import http

# class MrVideo(http.Controller):
#     @http.route('/mr_video/mr_video/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mr_video/mr_video/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mr_video.listing', {
#             'root': '/mr_video/mr_video',
#             'objects': http.request.env['mr_video.mr_video'].search([]),
#         })

#     @http.route('/mr_video/mr_video/objects/<model("mr_video.mr_video"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mr_video.object', {
#             'object': obj
#         })