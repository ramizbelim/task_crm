from odoo import models, fields

class CrmStage(models.Model):
    _inherit = "crm.stage"

    is_quote_ready_stage = fields.Boolean(string="Is Quote Ready Stage?")






