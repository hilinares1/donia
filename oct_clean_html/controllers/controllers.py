# -*- coding: utf-8 -*-
from odoo import http

# class OctMakeModules(http.Controller):
#     @http.route('/oct_clean_html/oct_clean_html/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oct_clean_html/oct_clean_html/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oct_make_modules.listing', {
#             'root': '/oct_clean_html/oct_clean_html',
#             'objects': http.request.env['oct_clean_html.oct_clean_html'].search([]),
#         })

#     @http.route('/oct_clean_html/oct_clean_html/objects/<model("oct_clean_html.oct_clean_html"):obj>/,auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oct_make_modules.object', {
#             'object': obj
#         })