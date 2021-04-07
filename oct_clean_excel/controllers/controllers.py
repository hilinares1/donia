# -*- coding: utf-8 -*-
# from odoo import http


# class OctCleanExcel(http.Controller):
#     @http.route('/oct_clean_excel/oct_clean_excel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oct_clean_excel/oct_clean_excel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oct_clean_excel.listing', {
#             'root': '/oct_clean_excel/oct_clean_excel',
#             'objects': http.request.env['oct_clean_excel.oct_clean_excel'].search([]),
#         })

#     @http.route('/oct_clean_excel/oct_clean_excel/objects/<model("oct_clean_excel.oct_clean_excel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oct_clean_excel.object', {
#             'object': obj
#         })
