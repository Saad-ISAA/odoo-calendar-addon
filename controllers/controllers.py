# -*- coding: utf-8 -*-
# from odoo import http


# class GoogleCalendar(http.Controller):
#     @http.route('/google_calendar/google_calendar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/google_calendar/google_calendar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('google_calendar.listing', {
#             'root': '/google_calendar/google_calendar',
#             'objects': http.request.env['google_calendar.google_calendar'].search([]),
#         })

#     @http.route('/google_calendar/google_calendar/objects/<model("google_calendar.google_calendar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('google_calendar.object', {
#             'object': obj
#         })
