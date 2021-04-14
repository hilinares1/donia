# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
import logging
_logger = logging.getLogger(__name__)


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    web_price_round = fields.Boolean(string='Valor Tienda Web', default=False)

    def _compute_price(self, price, price_uom, product, quantity=1.0, partner=False):
        """Compute the unit price of a product in the context of a pricelist application.
           The unused parameters are there to make the full context available for overrides.
        """
        self.ensure_one()
        convert_to_price_uom = (lambda price: product.uom_id._compute_price(price, price_uom))
        if self.compute_price == 'fixed':
            price = convert_to_price_uom(self.fixed_price)
        elif self.compute_price == 'percentage':
            price = (price - (price * (self.percent_price / 100))) or 0.0
        else:
            # complete formula
            price_limit = price
            price = (price - (price * (self.price_discount / 100))) or 0.0
            if self.price_round:
                price = tools.float_round(price, precision_rounding=self.price_round)

            if self.price_surcharge:
                price_surcharge = convert_to_price_uom(self.price_surcharge)
                price += price_surcharge

            if self.price_min_margin:
                price_min_margin = convert_to_price_uom(self.price_min_margin)
                price = max(price, price_limit + price_min_margin)

            if self.price_max_margin:
                price_max_margin = convert_to_price_uom(self.price_max_margin)
                price = min(price, price_limit + price_max_margin)

            valor = ""
            _logger.info("========= PRICE ======= %r " % price)
            _logger.info("========= MARCADO PARA WEB ======= %r " % self.web_price_round)
            if self.web_price_round:
                _logger.info("========= MARCADO PARA WEB ======= %r " % self.web_price_round)
                str_price = str(price)
                decimal = str_price.split(".")
                _logger.info("========= DECIMAL ======= %r " % decimal)
                valor = str(decimal[0]) + "."
                if int(decimal[1]) < 60:
                    valor += str(49)
                else:
                    valor += str(99)
            price = float(valor)
            _logger.info("========= FINAL PRICE ======= %r " % price)
        return price