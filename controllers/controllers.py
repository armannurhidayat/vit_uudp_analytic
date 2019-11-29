# -*- coding: utf-8 -*-
from odoo import http

# class VitUudpAnalytic(http.Controller):
#     @http.route('/vit_uudp_analytic/vit_uudp_analytic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_uudp_analytic/vit_uudp_analytic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_uudp_analytic.listing', {
#             'root': '/vit_uudp_analytic/vit_uudp_analytic',
#             'objects': http.request.env['vit_uudp_analytic.vit_uudp_analytic'].search([]),
#         })

#     @http.route('/vit_uudp_analytic/vit_uudp_analytic/objects/<model("vit_uudp_analytic.vit_uudp_analytic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_uudp_analytic.object', {
#             'object': obj
#         })