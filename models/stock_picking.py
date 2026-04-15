from odoo import api, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _get_view(self, view_id=None, view_type='form', **options):
        arch, view = super()._get_view(view_id=view_id, view_type=view_type, **options)
        if view_type == 'form':
            page_size = int(
                self.env['ir.config_parameter'].sudo().get_param(
                    'stock_picking_pagination.page_size', '80'
                )
            )
            for node in arch.xpath("//field[@name='move_ids']//list"):
                node.set('limit', str(page_size))
        return arch, view
