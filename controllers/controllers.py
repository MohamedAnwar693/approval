# -*- coding: utf-8 -*-
# from odoo import http


# class Approval(http.Controller):
#     @http.route('/approval/approval', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/approval/approval/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('approval.listing', {
#             'root': '/approval/approval',
#             'objects': http.request.env['approval.approval'].search([]),
#         })

#     @http.route('/approval/approval/objects/<model("approval.approval"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('approval.object', {
#             'object': obj
#         })
