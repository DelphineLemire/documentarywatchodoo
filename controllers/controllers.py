# -*- coding: utf-8 -*-
# from odoo import http


# class Documentary-watch-odoo(http.Controller):
#     @http.route('/documentary-watch-odoo/documentary-watch-odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/documentary-watch-odoo/documentary-watch-odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('documentary-watch-odoo.listing', {
#             'root': '/documentary-watch-odoo/documentary-watch-odoo',
#             'objects': http.request.env['documentary-watch-odoo.documentary-watch-odoo'].search([]),
#         })

#     @http.route('/documentary-watch-odoo/documentary-watch-odoo/objects/<model("documentary-watch-odoo.documentary-watch-odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('documentary-watch-odoo.object', {
#             'object': obj
#         })
