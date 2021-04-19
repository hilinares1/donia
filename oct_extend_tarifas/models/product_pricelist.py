# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.tools import float_compare
import logging

_logger = logging.getLogger(__name__)


class PriceList(models.Model):
    _inherit = "product.pricelist"

    def _compute_price_rule(self, products_qty_partner, date=False, uom_id=False):
        result = super(PriceList, self)._compute_price_rule(products_qty_partner, date=date, uom_id=uom_id)

        for item in result:

            price = result[item][0]
            list = result[item][1]

            list_price_item = self.env['product.pricelist.item'].browse(list)
            if list_price_item:
                list_root = list_price_item.pricelist_id
                if list_root and list_root.website_id:
                    min_price = list_price_item.min_price

                    final_price = 0
                    if float_compare(min_price, price, precision_digits=2) == 1:
                        final_price = min_price
                    elif float_compare(min_price, price, precision_digits=2) == -1:
                        final_price = price

                    result[item] = (final_price, list)

        return result


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    min_price = fields.Float(string='Precio Minimo')