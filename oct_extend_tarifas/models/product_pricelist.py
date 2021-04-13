# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    web_shop = fields.Boolean(string='Valor Tienda Web')
