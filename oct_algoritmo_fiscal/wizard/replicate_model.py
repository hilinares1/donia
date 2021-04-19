from odoo import models, fields, api, exceptions
from datetime import date, datetime, timedelta
from numpy import random
import logging

_logger = logging.getLogger(__name__)


class wizard_algoritmo(models.TransientModel):
    _name = 'wizard.algoritmo'

    """pickings_date_time = fields.Selection(
        [('a', 'Trimestre Enero-Marzo'), ('b', 'Trimestre Abril-Junio'), ('c', 'Trimestre Julio-Septiembre'),
         ('d', 'Trimestre Octubre-Diciembre'), ], string='Seleccione un rango de Fechas')"""
    date_before = fields.Date('Desde')
    date_after = fields.Date('Hasta')

    def apply_algoritmo(self):
        date_before = datetime.fromordinal(self.date_before.toordinal())
        date_after = datetime.fromordinal(self.date_after.toordinal()).replace(hour=23, minute=59, second=59,
                                                                               microsecond=999999)

        companies = [{'id': 1, 'payment_method_id': 1, 'journal_cash_id': 6, 'journal_pos_id': 9},
                     {'id': 2, 'payment_method_id': 7, 'journal_cash_id': 70, 'journal_pos_id': 69},
                     {'id': 3, 'payment_method_id': 9, 'journal_cash_id': 86, 'journal_pos_id': 85}, ]

        date_before = self.date_before
        date_after = self.date_after
        ref = 'Ventas de %s hasta %s' % (date_before, date_after)
        for company in companies:
            self.distribucion_binomial(company.get('id'), company.get('payment_method_id'), date_before, date_after)
            # self.asignacion_ticket(1, 4, sequence_id, date_before, date_after)
            # self.asignacion_ticket(1, 7, sequence_id, date_before, date_after)
            # self.asignacion_ticket(1, 16, sequence_id, date_before, date_after)
            self.borrar_arqueos_caja(company.get('id'), company.get('journal_cash_id'), date_before, date_after)
            self.borrar_asientos_viejos(company.get('id'), company.get('journal_pos_id'), date_before, date_after)
            self.generate_account_move(company.get('id'), date_before, date_after, ref)

    def distribucion_binomial(self, company_id, payment_method_id, date_before, date_after):
        # _logger.info("ME ENTRA EN LA FUNCION DISTRIBUCION BINOMIAL EN LA COMPAÑIA: %r", company_id)
        # _logger.info("ME ENTRA EN LA FUNCION DISTRIBUCION BINOMIAL PARA LA FECHA: %r", date_before)
        # _logger.info("ME ENTRA EN LA FUNCION DISTRIBUCION BINOMIAL PARA LA FECHA: %r", date_after)
        for order in self.env['pos.order'].search([('company_id', '=', company_id), ('amount_total', '>', 0),
                                                   ('payment_ids.payment_method_id.id', '=', payment_method_id),
                                                   ('date_order', '>=', date_before), ('date_order', '<=', date_after),
                                                   ('state', '=', 'done')]):
            if len(order.payment_ids.mapped('payment_method_id.id')) == 1:

                x = random.binomial(n=1, p=0.2, size=1)
                if x == 1:
                    order.write({'x_studio_b': True})
                    self._cr.commit()

    """def asignacion_ticket(self, company_id, tpv_id, sequence_id, date_before, date_after):
        for order in self.env['pos.order'].search(
                [('x_studio_b', '=', False), ('company_id', '=', company_id), ('config_id.id', '=', tpv_id),
                 ('date_order', '>=', date_before), ('date_order', '<=', date_after), ('numero_ticket', '=', '')]):
            order.write({'numero_ticket': self.env['ir.sequence'].search([('id', '=', sequence_id)])._next()})"""

    def borrar_arqueos_caja(self, company_id, journal_id, date_before, date_after):
        # _logger.info("ME ENTRA EN LA FUNCION BORRAR ARQUEOS CAJA EN LA COMPAÑIA: %r", company_id)
        # _logger.info("ME ENTRA EN LA FUNCION BORRAR ARQUEOS CAJA PARA LA FECHA: %r", date_before)
        # _logger.info("ME ENTRA EN LA FUNCION BORRAR ARQUEOS CAJA PARA LA FECHA: %r", date_after)
        for bank in self.env['account.bank.statement'].search(
                [('company_id', '=', company_id), ('date', '>=', date_before), ('date', '<=', date_after),
                 ('journal_id', '=', journal_id)]):
            bank.button_reopen()
            for line in bank.line_ids:
                line.button_cancel_reconciliation()
                line.unlink()
            bank.unlink()
            self._cr.commit()

    def borrar_asientos_viejos(self, company_id, journal_id, date_before, date_after):
        # _logger.info("ME ENTRA EN LA FUNCION BORRAR ASIENTOS VIEJOS EN LA COMPAÑIA: %r", company_id)
        # _logger.info("ME ENTRA EN LA FUNCION BORRAR ASIENTOS VIEJOS PARA LA FECHA: %r", date_before)
        # _logger.info("ME ENTRA EN LA FUNCION BORRAR ASIENTOS VIEJOS PARA LA FECHA: %r", date_after)
        acounts = self.env['account.move'].search(
            [('ref', 'ilike', 'POS/0'), ('date', '>=', date_before), ('date', '<=', date_after),
             ('journal_id', '=', journal_id),
             ('company_id', '=', company_id)]).mapped('id')
        for id in acounts:
            try:
                account = self.env['account.move'].browse(id)
                account.button_draft()
                account.button_cancel()
                account.with_context({'force_delete': True}).unlink()
            except Exception as e:
                _logger.info('EXPETION ============ %r', [e])
            self._cr.commit()

    def generate_account_move(self, company_id, date_before, date_after, ref):

        if company_id in self.env.companies.mapped('id'):

            base_account_move = self.env['res.company'].browse(company_id).template_account_move_id

            new_account_move = base_account_move.copy(
                default={'date': date_after, 'ref': ref, 'company_id': company_id})
            sales_total = round(sum(self.env['pos.order'].search(
                [('company_id', '=', company_id), ('date_order', '>=', date_before), ('date_order', '<=', date_after),
                 ('state', '=', 'done')]).mapped('amount_total')), 2)
            sales_b = round(sum(self.env['pos.order'].search(
                [('company_id', '=', company_id), ('date_order', '>=', date_before), ('date_order', '<=', date_after),
                 ('state', '=', 'done'), ('x_studio_b', '=', True)]).mapped('amount_total')), 2)
            sales_wo_tax = round((sales_total - sales_b) / 1.21, 2)
            tax = round(sales_wo_tax * 21 / 100, 2)
            method_of_payments = self.env['pos.payment.method'].search([('company_id', '=', company_id)])
            pays_vals = []
            for method_of_payment in method_of_payments:
                amount = round(sum(self.env['pos.payment'].search(
                    [('company_id', '=', company_id), ('payment_method_id', '=', method_of_payment.id),
                     ('payment_date', '>=', date_before), ('payment_date', '<=', date_after),
                     ('pos_order_id.state', '=', 'done')]).mapped('amount')), 2)

                if method_of_payment.is_cash_count:
                    amount = round(amount - sales_b, 2)
                pays_vals.append(
                    {'payment_method_id': method_of_payment.id, 'is_cash_count': method_of_payment.is_cash_count,
                     'amount': amount, 'name': method_of_payment.name})
            new_lines = []
            for line in new_account_move.line_ids:
                if '47700' in line.account_id.code:
                    new_lines.append((1, line.id, {
                        'move_id': new_account_move.id,
                        'account_id': line.account_id.id,
                        'name': line.name,
                        'credit': tax

                    }))
                    # _logger.info("=====TAX====%r", [tax])

                if '700000000' in line.account_id.code:
                    new_lines.append((1, line.id, {
                        'move_id': new_account_move.id,
                        'account_id': line.account_id.id,
                        'name': line.name,
                        'credit': sales_wo_tax

                    }))
                    # _logger.info("=====SaleWhitout====%r", [sales_wo_tax])

                if '43010' in line.account_id.code:
                    for pay in pays_vals:
                        if pay.get('amount') < 0:
                            new_lines.append((1, line.id, {
                                'move_id': new_account_move.id,
                                'account_id': line.account_id.id,
                                'name': pay.get('name'),
                                'debit': 0,
                                'credit': abs(pay.get('amount'))

                            }))
                        else:
                            new_lines.append((1, line.id, {
                                'move_id': new_account_move.id,
                                'account_id': line.account_id.id,
                                'name': pay.get('name'),
                                'debit': pay.get('amount'),
                                'credit': 0

                            }))

                        pays_vals.remove(pay)
                        # _logger.info("=====PAY====%r", [pay.get('name'), pay.get('amount')])
                        break
            # new_account_move.line_ids.unlink()
            # _logger.info("==========%r", new_lines)
            new_account_move.write({'line_ids': new_lines})

            # _logger.info("============%r", [sales_total, sales_b, sales_wo_tax])
