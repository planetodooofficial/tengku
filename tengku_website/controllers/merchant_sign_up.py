from odoo import http
from odoo.http import request
import json

class MerchantSignUpWebPage(http.Controller):

    # @http.route('/sign-up/page', type='http', auth="user")
    # def signup(self, **kw):
    #     return http.request.render('tengku_website.create_page', {})

    @http.route('/create/merchantwebuser', type="http", auth="public", website=True)
    def merchant_user(self, **post):
        print("Data Received.....", post)
        # request.env['res.users'].sudo().create(kw)
        user_val1 = {
            'name': post.get('org_name1'),
            'login': post.get('email1'),
        }
        request.env['res.users'].sudo().create(user_val1)

        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('org_name1'))])

        partner_search.sudo().update({
            'org_nick_name': post.get('nick_name'),
            'company_type': 'company',
            'email': post.get('email1'),
            'street': post.get('address1'),
            'street2': post.get('address2'),
            # 'center_type': post.get('mul_selection1'),
            # 'types': post.get('mul_selection1'),
            'city': post.get('city2'),
            'state_id': post.get('state2'),
            'country_id': 157,
            'zip': post.get('code1'),
            'gps_coordinates': post.get('coordinates'),
            'registration_no': post.get('reg_no'),
            'description': post.get('descrption'),
            'phone': post.get('tel_no'),
            'mobile': post.get('mobile_no'),
            'website': post.get('website_1'),
            'twitter_url': post.get('url'),
            'fb_url': post.get('url1'),
            'insta_url': post.get('url2'),
            # 'supplier_rank': 1,
        })

        value = {'res_id': partner_search}

        return request.render('tengku_website.merchantaccount2', value)


    @http.route('/create/merchantpartners', type="http", auth="public", website=True)
    def merchant_partners(self, **post):

        main_partner_search = http.request.env['res.partner'].sudo().search([('id', '=', post.get('res_id'))])

        user_val = {
            'name': post.get('mer_mem_1'),
            'login': post.get('email11')
        }

        request.env['res.users'].sudo().create(user_val)

        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('mer_mem_1'))])

        partner_search.sudo().update({
            # 'type': 'delivery',
            'company_type': 'person',
            # 'name': post.get('org_name') + Shipping Address,
            'street': post.get('address1'),
            'street2': post.get('address2'),
            'city': post.get('city2'),
            'state_id': post.get('state2'),
            'country_id': 157,
            'email': post.get('email11'),
            'zip': post.get('code1'),

            'parent_id': main_partner_search.id,
        })

        user_val = {
            'name': post.get('mer_mem_2'),
            'login': post.get('email12'),
        }

        request.env['res.users'].sudo().create(user_val)

        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('mer_mem_2'))])

        partner_search.sudo().update({
            # 'type': 'delivery',
            'company_type': 'person',
            'email': post.get('email12'),
            'parent_id': main_partner_search.id,
        })

        user_val = {
            'name': post.get('mer_mem_3'),
            'login': post.get('email13'),
        }

        request.env['res.users'].sudo().create(user_val)

        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('mer_mem_3'))])

        partner_search.sudo().update({
            # 'type': 'delivery',
            'company_type': 'person',
            'email': post.get('email13'),
            'parent_id': main_partner_search.id,
        })

        value = {'res_id': partner_search}

        return request.render('tengku_website.merchantthankyou', {})


