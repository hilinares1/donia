# -*- coding: utf-8 -*-
from odoo import http

# class OctMakeModules(http.Controller):
#     @http.route('/oct_extend_tarifas/oct_extend_tarifas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oct_extend_tarifas/oct_extend_tarifas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oct_make_modules.listing', {
#             'root': '/oct_extend_tarifas/oct_extend_tarifas',
#             'objects': http.request.env['oct_extend_tarifas.oct_extend_tarifas'].search([]),
#         })

#     @http.route('/oct_extend_tarifas/oct_extend_tarifas/objects/<model("oct_extend_tarifas.oct_extend_tarifas"):obj>/,auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oct_make_modules.object', {
#             'object': obj
#         })