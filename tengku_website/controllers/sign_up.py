from odoo import http
from odoo.http import request
import json

class SignUpWebPage(http.Controller):

    # @http.route('/sign-up/page', type='http', auth="user")
    # def signup(self, **kw):
    #     return http.request.render('tengku_website.create_page', {})

    @http.route('/create/webuser', type="http", auth="public", website=True)
    def create_webuser(self, **post):
        print("Data Received.....", post)
        # request.env['res.users'].sudo().create(kw)
        user_val = {
            'name': post.get('org_name'),
            'login': post.get('email'),
        }
        request.env['res.users'].sudo().create(user_val)

        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('org_name'))])

        partner_search.update({
            'org_nick_name': post.get('org_nick_name'),
            'company_type': 'company',
            'email': post.get('email'),
            'street': post.get('register_address_line1'),
            'street2': post.get('register_address_line2'),
            'city': post.get('register_address_city'),
            # 'state_id': post.get('register_address_state'),
            'country_id': 157,
            'zip': post.get('register_address_pin_code'),
            'gps_coordinates': post.get('register_address_gps'),
            'registration_no': post.get('ros_registration'),
            'description': post.get('descp'),
            'phone': post.get('phone'),
            'mobile': post.get('mobile'),
        })

        value={'res_id': partner_search}


        return request.render('tengku_website.accountpage', value)



    @http.route('/create/create/user', type="http", auth="public", website=True)
    def create_user(self, **post):

        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('res_id'))])

        partner_search.update({

        })

        return request.render('tengku_website.accountpage', {})