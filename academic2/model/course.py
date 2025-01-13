#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class course(models.Model):

    _name = "vit.course"
    _description = "vit.course"


    def action_reload(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    description = fields.Text( string=_("Description"))


    session_ids = fields.One2many(comodel_name="vit.session",  inverse_name="course_id",  string=_("Session"))
