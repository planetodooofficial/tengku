from odoo import http
from odoo.http import request
import json

class SignUpWebPage(http.Controller):

    @http.route('/sign-up/page', type='http', auth="user")
    def signup(self, **kw):
        return http.request.render('tengku_website.create_page', {})
