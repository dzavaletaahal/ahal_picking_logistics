# -*- coding: utf-8 -*-
from odoo import fields, models, api, _

class FleteRel(models.Model):
    _name = 'flete.rel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Flete Rel'
    _rec_name ='name'

    #FIELDS FOR NEW MODEL FLETE REL
    name = fields.Char(string="Flete")
    flete_partner = fields.Many2one('res.partner',string="Proveedor Flete")
    flete_id = fields.Integer(string="Número ID")
    flete_date_con = fields.Date(string="Fecha contrato")
    flete_date_disp = fields.Date(string="Fecha Disponibilidad")
    flete_asigna = fields.Char(string="Lugar de asignación")

    flete_status =  fields.Selection(
        selection=[('disponible', 'Disponible'), 
                   ('viaje_mp', 'Viaje Materia Prima'),
                   ('viaje_pt', 'Viaje Producto Terminado')],
        string=('Estatus de la unidad'),default="disponible", track_visibility='always'
    )


    flete_car_id = fields.Integer(string="Identificación de la unidad")

    #MANY2MANY FIELD FOR TAGS
    flete_label = fields.Many2many('flete.labels', 'name', string="Etiquetas")

    flete_place_out = fields.Char(string="Lugar fin de asignación")
    flete_date_out = fields.Date(string="Fecha de retiro asignación")
    flete_obs = fields.Text(string="Observaciones")

    restart_state = fields.Boolean(string="Restablecer a disponible", help="Utilizar restablecer a disponible, recomendado en fletes seleccionados por error en los picking")

    #FUNCTION TO CHANGE STATE WHEN THE RESTART FLETE IS CHANGED
    @api.onchange('restart_state')
    def get_flete_status(self):
        for rec in self:
            if rec.restart_state == True:
                rec.flete_status = 'disponible'

    picking_id = fields.Many2one('stock.picking', string="Picking", compute="get_picking", track_visibility='always')

    #SHOW THE PICKING ID IN THE MODEL FLETE
    def get_picking(self):
        for rec in self:
            rec.picking_id = rec.env['stock.picking'].search([('flete_id.name', '=', rec.name), ('state', '!=', 'done')], limit=1, order="create_date desc")
 




class FleteLabels(models.Model):
    _name = 'flete.labels'
    _description = 'Flete Labels'
    _rec_name ='name'    

    name = fields.Char(string="Nombre")

