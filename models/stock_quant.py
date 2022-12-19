# -*- coding: utf-8 -*-

from odoo import models, api, fields, _

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    kd_cargo = fields.Date(string="Killing date")
    flete_id = fields.Many2one('flete.rel',string="Flete")
    fecha_entrada = fields.Date(string="Fecha entrada")

