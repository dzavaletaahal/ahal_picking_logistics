# -*- coding: utf-8 -*-
##############################################################################
#                 @author AHAL
#
##############################################################################

{
    'name': 'AHAL Picking Logistics',
    'version': '1.1',
    'description': ''' Picking logistics form
    ''',
    'category': 'Inventory',
    'author': 'AHAL Consultores',
    'website': '',
    'depends': [
        'stock','mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_view.xml',
        'views/flete_rel_view.xml',
        'views/plant_view.xml',
        'views/logistics_report_tree_view.xml',
        'views/stock_quant_view.xml',
    ],
    'images': [],
    'application': False,
    'installable': True,
    'price': 0.00,
    'currency': 'USD',
    'license': 'OPL-1',
}
