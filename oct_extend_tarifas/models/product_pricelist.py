# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _

class PricelistItem(models.Model):
    _name = "product.pricelist.item"

    compute_price = fields.Selection(selection_add=[('fisica', "Tienda Fisica"),('web', "Tienda Web")])