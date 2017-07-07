# -*- coding: utf-8 -*-
from odoo import http

# class Openaccademy(http.Controller):
#     @http.route('/openaccademy/openaccademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openaccademy/openaccademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openaccademy.listing', {
#             'root': '/openaccademy/openaccademy',
#             'objects': http.request.env['openaccademy.openaccademy'].search([]),
#         })

#     @http.route('/openaccademy/openaccademy/objects/<model("openaccademy.openaccademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openaccademy.object', {
#             'object': obj
#         })