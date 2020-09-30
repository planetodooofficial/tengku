from odoo import fields, models, api, _

class TengkuWebsiteInherit(models.Model):

    _inherit = 'res.partner'

    org_nick_name = fields.Char("Organization Nick name")
    registration_no = fields.Integer("Registration no")
    description = fields.Text("Description")
    center_type = fields.Selection([('animal', 'Animal'), ('arts_and_culture', 'Arts & Culture'),
                                    ('children', 'Children'), ('diff_abled', 'Different Abled'),
                                    ('edu_talent', 'Education & Talent'), ('emg_dist', 'Emergency & Disaster'),
                                    ('env', 'Enviornment'), ('health', 'Health'), ('sr_ctz', 'Senior Citizen'),
                                    ('tax_exempt', 'Tax Exemption'), ('women', 'Women'), ('youth', 'Youth'),
                                    ('others', 'Others')], string="Type")
    gps_coordinates = fields.Integer("GPS Co-Ordinates")

    twitter_url = fields.Char('Twitter Link')
    fb_url = fields.Char('Facebook Link')
    insta_url = fields.Char('Instagram Link')

    bank_acc = fields.Char("Bank Account")
    bank_acc_name = fields.Char("Bank Name")