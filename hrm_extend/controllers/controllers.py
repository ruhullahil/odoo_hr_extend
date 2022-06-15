# -*- coding: utf-8 -*-
# from odoo import http


# class HrmExtend(http.Controller):
#     @http.route('/hrm_extend/hrm_extend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hrm_extend/hrm_extend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hrm_extend.listing', {
#             'root': '/hrm_extend/hrm_extend',
#             'objects': http.request.env['hrm_extend.hrm_extend'].search([]),
#         })

#     @http.route('/hrm_extend/hrm_extend/objects/<model("hrm_extend.hrm_extend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hrm_extend.object', {
#             'object': obj
#         })
