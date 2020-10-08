from odoo import fields, models, api, _

class TypeOrgMultiSelect(models.Model):

    _name = 'type.org.multi.select'

    _rec_name = "type_name"
    type_name = fields.Selection([('animal', 'Animal'), ('arts_and_culture', 'Arts & Culture'),
                                    ('children', 'Children'), ('diff_abled', 'Different Abled'),
                                    ('edu_talent', 'Education & Talent'), ('emg_dist', 'Emergency & Disaster'),
                                    ('env', 'Enviornment'), ('health', 'Health'), ('sr_ctz', 'Senior Citizen'),
                                    ('tax_exempt', 'Tax Exemption'), ('women', 'Women'), ('youth', 'Youth'),
                                    ('others', 'Others')], string="Type")
