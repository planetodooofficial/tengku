from odoo import http
from odoo.http import request
import json

class SignUpWebPage(http.Controller):

    # @http.route('/sign-up/page', type='http', auth="user")
    # def signup(self, **kw):
    #     return http.request.render('tengku_website.create_page', {})

    @http.route('/create/webuser', type="http", auth="public", website=True)
    def create_webuser(self, **kw):
        print("Data Received.....", kw)
        # request.env['res.users'].sudo().create(kw)
        user_val = {
            'name': kw.get('org_nick_name')
        }
        request.env['res.users'].sudo().create(user_val)
        return request.render("tengku_website.registration", {})

