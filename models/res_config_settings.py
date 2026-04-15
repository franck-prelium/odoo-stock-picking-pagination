from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    stock_picking_page_size = fields.Integer(
        string='Lignes par page dans les transferts',
        default=80,
        config_parameter='stock_picking_pagination.page_size',
        help=(
            'Nombre de lignes affichées par page dans l\'onglet Opérations '
            'des bons de livraison et transferts. Par défaut : 80.'
        ),
    )
