#-*- coding: utf-8 -*-

from odoo import models, fields, api


class pos_tpv(models.Model):
    _inherit = 'pos.order'


    numero_ticket = fields.Char(string='Nro. Ticket', readonly=False, copy=False)


class ResCompany(models.Model):
    _inherit = 'res.company'
    template_account_move_id = fields.Many2one(comodel_name='account.move', string='Plantilla de Asiento Contable')




