from odoo import fields, models, api, _

class ResCity(models.Model):

    _name = 'res.city'

    name = fields.Char('name')
    state_id = fields.Many2one('res.country.state')