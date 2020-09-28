from odoo import fields, models, api, _

class TengkuWebsiteInherit(models.Model):

    _inherit = 'res.partner'

    org_nick_name = fields.Char("Organization Nick name:")
    registration_no = fields.Integer("Registration no:")
    description = fields.Text("Description:")
    type = fields.Char("Type:")
    gps_coordinates = fields.Integer("GPS Co-Ordinates:")