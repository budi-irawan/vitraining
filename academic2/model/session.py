#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class session(models.Model):

    _name = "vit.session"
    _description = "vit.session"


    def action_reload(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    description = fields.Text( string=_("Description"))
    start_date = fields.Date( string=_("Start Date"))
    duration = fields.Integer( string=_("Duration"))


    course_id = fields.Many2one(comodel_name="vit.course",  string=_("Course"))
