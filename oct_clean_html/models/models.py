# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class oct_clean_html(models.Model):
#     _name = 'oct_clean_html.oct_clean_html'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100