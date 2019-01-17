# -*- coding: utf-8 -*-
from odoo import http

# class Odoogedon(http.Controller):
#     @http.route('/odoogedon/odoogedon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoogedon/odoogedon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoogedon.listing', {
#             'root': '/odoogedon/odoogedon',
#             'objects': http.request.env['odoogedon.odoogedon'].search([]),
#         })

#     @http.route('/odoogedon/odoogedon/objects/<model("odoogedon.odoogedon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoogedon.object', {
#             'object': obj
#         })