# -*- coding: utf-8 -*-
# from odoo import http


# class DkTransportManagement(http.Controller):
#     @http.route('/dk_transport_management/dk_transport_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dk_transport_management/dk_transport_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dk_transport_management.listing', {
#             'root': '/dk_transport_management/dk_transport_management',
#             'objects': http.request.env['dk_transport_management.dk_transport_management'].search([]),
#         })

#     @http.route('/dk_transport_management/dk_transport_management/objects/<model("dk_transport_management.dk_transport_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dk_transport_management.object', {
#             'object': obj
#         })
