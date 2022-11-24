# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    _sql_constraints = [
        ('client_order_ref_partner_uniq', 'unique(client_order_ref, partner_id)',
         _('Client order ref must be unique by customer!')),
    ]
