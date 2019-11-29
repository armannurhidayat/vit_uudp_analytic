# -*- coding: utf-8 -*-

from odoo import models, fields, api

class uudp(models.Model):
    _name = 'uudp'
    _inherit = 'uudp'

    location_id = fields.Many2one(
        'account.analytic.tag',
        string='Location',
    )

    business_id = fields.Many2one(
        'account.analytic.tag',
        string='Business',
    )