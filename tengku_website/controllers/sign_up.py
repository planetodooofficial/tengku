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
            'city_id': post.get('register_address_city'),
            'state_id': post.get('register_address_state'),
            'country_id': 157,
            'zip': post.get('register_address_pin_code'),
            'gps_coordinates': post.get('register_address_gps'),
            'registration_no': post.get('ros_registration'),
            'description': post.get('descp'),
            'phone': post.get('phone'),
            'mobile': post.get('mobile'),
            'supplier_rank': 1,
        })


        ship_vals = {
            'type': 'delivery',
            'name': post.get('org_name')+ 'Shipping Address',
            'street': post.get('shipping_address_line1'),
            'street2': post.get('shipping_address_line2'),
            'city_id': post.get('shipping_address_city'),
            'state_id': post.get('shipping_address_state'),
            'country_id': 157,
            'zip': post.get('shipping_address_pin_code'),
            'parent_id': partner_search.id,

        }



        ship_addr_obj= request.env['res.users'].sudo().create(ship_vals)


        value={'res_id': partner_search}


        return request.render('tengku_website.accountpage', value)



    @http.route('/create/create/user', type="http", auth="public", website=True)
    def create_user(self, **post):

        partner_search = http.request.env['res.partner'].sudo().search([('id', '=', post.get('res_id'))])

        partner_search.update({
            'bank_acc_name': post.get('bank_name'),
            # 'bank_acc': post.get('bank_name'),
            'website_url': post.get('website_domain'),
            'twitter_url': post.get('twitter_domain'),
            'fb_url': post.get('fb_domain'),
            'insta_url': post.get('insta_domain'),

        })

        value = {'res_id': partner_search}

        return request.render('tengku_website.accountpage2', value)



    @http.route('/create/partners', type="http", auth="public", website=True)
    def create_partners(self, **post):

        main_partner_search = http.request.env['res.partner'].sudo().search([('id', '=', post.get('res_id'))])

        user_val = {
            'name': post.get('member_name1'),
            'login': post.get('email_id1'),
        }

        request.env['res.users'].sudo().create(user_val)

        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('member_name1'))])

        partner_search.update({
            'company_type': 'person',
            'parent_id': main_partner_search.id,
        })

        value = {'res_id': partner_search}


        return request.render('tengku_website.thankyou', {})






    @http.route('/get_state', auth='public', type='http', website=True, methods=['POST'], csrf=False)
    def get_state(self, **kw):

        city_ids = request.env['res.country.state'].sudo().search([('country_id', '=', 157)])
        data = {}
        state_list = []
        for state in city_ids:
            state_list.append({'id': state.id, 'value': state.name})

        if state_list:
            data['states'] = state_list
        return json.dumps(data)
    

    @http.route('/get_city', auth='public', type='http', website=True, methods=['POST'], csrf=False)
    def get_city_func(self, state, **kw):
        city_list = []
        if state:
            city_ids = request.env['res.city'].search([('state_id', '=', int(state))])
            for city in city_ids:
                city_list.append({'id': city.id, 'value': city.name})
        return json.dumps(city_list)