# -*- coding: utf-8 -*-

from odoo import models, api, fields, _

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    kd_cargo = fields.Date(string="Killing date")
    flete_id = fields.Many2one('flete.rel',string="Flete")
    fecha_entrada = fields.Date(string="Fecha entrada")

    @api.model
    def _get_inventory_fields_write(self):    
        fields = super(StockQuant, self)._get_inventory_fields_write()     
        return fields + ['kd_cargo', 'flete_id', 'fecha_entrada'] 

