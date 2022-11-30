# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
import json

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    calculo_cargo =  fields.Selection(
        selection=[('calc_diff', 'Calcular diferencias'), 
                   ('no_calc', 'Sin calculo(Pago a Val. De factura)'),],
        string=('Estatus de cálculo'),
    )

    plant_cargo =  fields.Selection(
        selection=[('sumter', 'SUMTER FRESH PLANT'), 
                   ('douglas', 'DOUGLAS GA'),
                   ('columbia', 'COLUMBIA'),
                   ('bryan', 'BRYAN TX')],
        string=('PLANT'), default='sumter',
    )

    kd_cargo = fields.Date(string="KILLING DATE")
    pd_cargo = fields.Date(string="PACKING DATE")
    gw_usa_cargo = fields.Float(string="GROSS WEIGTH SCALE USA")
    tare_cargo = fields.Float(string="TARE")
    water_spill_cargo = fields.Float(string="WATER SPILL")
    rejections_fq_cargo = fields.Float(string="REJECTIONS FOR QUALITY")
    net_weigth_usa_cargo = fields.Float(string="NET WEIGTH SCALE USA", compute="get_net_weigth")
    weigth_in_cargo = fields.Float(string="WEIGTH INVOICED")
    diff_weigth_ampasa_cargo = fields.Float(string="DIFERENCE WEIGTH AMPASA", compute="get_diff_weigth")
    combos_cargo = fields.Float(string="COMBOS")
    price_cargo = fields.Float(string="PRICE")
    cost_cargo = fields.Float(string="COST", compute="get_cost")
    obs_cargo = fields.Text(string="OBSERVATIONS")

    flete_id = fields.Many2one('flete.rel',string="Flete", track_visibility='always')

    #CREATE FUNCTION TO GET THE FLETE STATUS DINAMICALLY
    #BUSCA LOS REGISTROS DONDE ESTE SELECCIONADO EL FLETE
    

    #FUNCTION TO CHANGE STATE WHEN THE FLETE IS SELECTED
    @api.onchange('flete_id')
    def get_flete_status(self):
        for rec in self:
            if rec.picking_type_id.sequence_code == 'IN':
                rec.flete_id.flete_status = 'viaje_mp'
            elif rec.picking_type_id.sequence_code == 'OUT':
                rec.flete_id.flete_status = 'viaje_pt'
            else:
                rec.flete_id.flete_status = 'disponible'

    #FUNCTION TO WRITE THE FLETE AS DISPONIBLE WHEN THE STATE IS DONE
    def _compute_state(self):
        res = super(StockPicking, self)._compute_state()
        if self.state == 'done':
            self.flete_id.write({'flete_status': 'disponible'})
            return res



    
    def get_net_weigth(self):
        for rec in self:
            rec.net_weigth_usa_cargo = rec.gw_usa_cargo - rec.tare_cargo - rec.water_spill_cargo - rec.rejections_fq_cargo
     

    def get_diff_weigth(self):
        for rec in self:
            rec.diff_weigth_ampasa_cargo = rec.net_weigth_usa_cargo - rec.weigth_in_cargo
     

    def get_cost(self):
        for rec in self:
            rec.cost_cargo = rec.diff_weigth_ampasa_cargo - rec.price_cargo
     