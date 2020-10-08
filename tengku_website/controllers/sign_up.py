from odoo import http
from odoo.http import request
import json
import base64


class SignUpWebPage(http.Controller):

    # @http.route('/sign-up/page', type='http', auth="user")
    # def signup(self, **kw):
    #     return http.request.render('tengku_website.create_page', {})

    @http.route('/vendor_type', type="http", auth="public", website=True)
    def def_vendor_type(self, **post):
        print(post)

        value= {'vendor_type': post.get('vendor_selection')}

        if post.get('vendor_selection') == 'center':

            return request.render('tengku_website.registration', value)




    @http.route('/create/webuser', type="http", auth="public", website=True)
    def create_webuser(self, **post):
        print("Data Received.....", post)
        # request.env['res.users'].sudo().create(kw)

        if post.get('attachment', False):
            self.attachment_ = request.env['ir.attachment']
            Attachments = self.attachment_
            name = post.get('attachment').filename
            file = post.get('attachment')
            attachment = file.read()

            user_val = {
                'name': post.get('org_name'),
                'login': post.get('email'),
                'image_1920': base64.standard_b64encode(attachment),
            }

            request.env['res.users'].sudo().create(user_val)

        else:

            user_val = {
                'name': post.get('org_name'),
                'login': post.get('email'),
            }

            request.env['res.users'].sudo().create(user_val)


        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('org_name'))])

        partner_search.sudo().update({
            'org_nick_name': post.get('org_nick_name'),
            'company_type': 'company',
            'email': post.get('email'),
            'street': post.get('register_address_line1'),
            'street2': post.get('register_address_line2'),

            'center_type': post.get('type'),
            # 'types': post.get('type'),

            # 'city_id': post.get('register_address_city'),
            'state_id': post.get('register_address_state'),
            'country_id': 157,
            'zip': post.get('register_address_pin_code'),
            'gps_coordinates': post.get('register_address_gps'),
            'registration_no': post.get('ros_registration'),
            'description': post.get('descp'),
            'phone': post.get('phone'),
            'mobile': post.get('mobile'),
            # 'supplier_rank': 1,
        })

        # partner_search.child_ids.sudo().update({
        #      'type': 'delivery',
        #     # 'search_default_type': 'delivery',
        #      'name': post.get('org_name')+ 'Shipping Address',
        #      'street': post.get('shipping_address_line1'),
        #      'street2': post.get('shipping_address_line2'),
        #      # 'city_id': post.get('shipping_address_city'),
        #      'state_id': post.get('shipping_address_state'),
        #      'country_id': 157,
        #      'zip': post.get('shipping_address_pin_code'),
        #      'parent_id': partner_search.id,
        #
        #     })



        # ship_vals = {
        #     'type': 'delivery',
        #     'name': post.get('org_name')+ 'Shipping Address',
        #     'street': post.get('shipping_address_line1'),
        #     'street2': post.get('shipping_address_line2'),
        #     'city_id': post.get('shipping_address_city'),
        #     'state_id': post.get('shipping_address_state'),
        #     'country_id': 157,
        #     'zip': post.get('shipping_address_pin_code'),
        #     'parent_id': partner_search.id,
        #
        # }
        #
        #
        #
        # ship_addr_obj= request.env['res.users'].sudo().create(ship_vals)

        # ship_addr_obj = request.env['res.users'].sudo().create(ship_vals)


        value = {'res_id': partner_search}


        return request.render('tengku_website.accountpage', value)



    @http.route('/create/create/user', type="http", auth="public", website=True)
    def create_user(self, **post):

        partner_search = http.request.env['res.partner'].sudo().search([('id', '=', post.get('res_id'))])

        partner_search.sudo().update({
            'bank_acc_name': post.get('bank_name'),
            'bank_acc': post.get('acc_no'),
            'website': post.get('website_domain'),
            'twitter_url': post.get('twitter_domain'),
            'fb_url': post.get('fb_domain'),
            'insta_url': post.get('insta_domain'),

        })

        if post.get('registration_attachment', False):
            self.attachment_ = request.env['ir.attachment']
            Attachments = self.attachment_
            name = post.get('registration_attachment').filename
            file = post.get('registration_attachment')
            attachment = file.read()
            attachment_id = Attachments.sudo().create({
                'name': name,
                'display_name': name,
                'res_name': name,
                'type': 'binary',
                'res_model': 'res.partner',
                'res_id': partner_search.id,
                # 'datas': attachment.encode('base64'),
                'datas': base64.standard_b64encode(attachment)
            })

            partner_search.update({
                'registration_acth': base64.standard_b64encode(attachment),
                'file_name': name,
            })


        if post.get('bank_st_front_pg_attachment', False):
            self.attachment_ = request.env['ir.attachment']
            Attachments = self.attachment_
            name = post.get('bank_st_front_pg_attachment').filename
            file = post.get('bank_st_front_pg_attachment')
            attachment = file.read()
            attachment_id = Attachments.sudo().create({
                'name': name,
                'display_name': name,
                'res_name': name,
                'type': 'binary',
                'res_model': 'res.partner',
                'res_id': partner_search.id,
                # 'datas': attachment.encode('base64'),
                'datas': base64.standard_b64encode(attachment)
            })

            partner_search.update({
                'front_page_bank_st': base64.standard_b64encode(attachment),
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

        partner_search.sudo().update({
            'type': 'contact',
            'company_type': 'person',
            'parent_id': main_partner_search.id,
        })

        user_val = {
            'name': post.get('member_name2'),
            'login': post.get('email_id2'),
        }

        request.env['res.users'].sudo().create(user_val)

        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('member_name2'))])

        partner_search.sudo().update({
            'type': 'contact',
            'company_type': 'person',
            'parent_id': main_partner_search.id,
        })

        user_val = {
            'name': post.get('member_name3'),
            'login': post.get('email_id3'),
        }

        request.env['res.users'].sudo().create(user_val)

        partner_search = http.request.env['res.partner'].sudo().search([('name', '=', post.get('member_name3'))])

        partner_search.sudo().update({
            'type': 'contact',
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
            city_ids = request.env['res.city'].sudo().search([('state_id', '=', int(state))])
            for city in city_ids:
                city_list.append({'id': city.id, 'value': city.name})
        return json.dumps(city_list)