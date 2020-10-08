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

    city_id = fields.Many2one('res.city', 'City')

    # website_url = fields.Char('Website Link')
    twitter_url = fields.Char('Twitter Link')
    fb_url = fields.Char('Facebook Link')
    insta_url = fields.Char('Instagram Link')

    bank_acc = fields.Char("Bank Account")
    bank_acc_name = fields.Selection([('abb', 'Affin Bank Berhad'), ('abmb', 'Alliance Bank Malaysia Berhad'),
                                    ('ab', 'AmBank (M) Berhad'),('bbb', 'Bangkok Bank Berhad'),('bamb', 'Bank of America Malaysia Berhad'),
                                      ('bcb', 'Bank of China (Malaysia) Berhad'),('btmu', 'Bank of Tokyo-Mitsubishi UFJ (Malaysia) Berhad'),('cbb', 'CIMB Bank Berhad'),
                                      ('cb', 'Citibank Berhad'),('dbb', 'Deutsche Bank (Malaysia) Berhad'),('ebb', 'EON Bank Berhad'),
                                      ('hlbb', 'Hong Leong Bank Berhad'),('hbmb', 'HSBC Bank Malaysia Berhad'),('icbc', 'Industrial and Commercial Bank of China (Malaysia) Berhad'),
                                      ('jp', 'J.P. Morgan Chase Bank Berhad'),('mbb', 'Malayan Banking Berhad'),('obb', 'OCBC Bank (Malaysia) Berhad'),('pbb', 'Public Bank Berhad'),
                                      ('rbb', 'RHB Bank Berhad'),('scbmb', 'Standard Chartered Bank Malaysia Berhad'),('smbcmb', 'Sumitomo Mitsui Banking Corporation Malaysia Berhad'),
                                      ('bns', 'The Bank of Nova Scotia Berhad'),('rbs', 'The Royal Bank of Scotland Berhad'),('uob', 'United Overseas Bank (Malaysia) Bhd')], string="Bank Name")

    is_merchant = fields.Boolean("Is Merchant")
    is_organization = fields.Boolean("Is Organization")


    # registration_attachment_id = fields.Many2one('ir.attachment', string='Attachment', ondelete='cascade')
    registration_acth = fields.Binary(string='Registration Certificate')
    file_name = fields.Char("File Name")


    front_page_bank_st = fields.Binary(string='Bank Statement Front Page')

    types = fields.Many2many('type.org.multi.select', string='Type')
