
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        result = super(SaleOrderInherit, self).action_confirm()
        vals= {
            'name': self.name,
            'start': self.commitment_date,
            'stop': self.commitment_date,
            'duration':0.5,
            }
        calendar_event = self.env['calendar.event']
        calendar_event.create(vals)
        self.env.cr.commit()
        return result