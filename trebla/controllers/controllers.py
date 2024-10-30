# -*- coding: utf-8 -*-
# from odoo import http


# class Trebla(http.Controller):
#     @http.route('/trebla/trebla', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trebla/trebla/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trebla.listing', {
#             'root': '/trebla/trebla',
#             'objects': http.request.env['trebla.trebla'].search([]),
#         })

#     @http.route('/trebla/trebla/objects/<model("trebla.trebla"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trebla.object', {
#             'object': obj
#         })

