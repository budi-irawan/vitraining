#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class user(models.Model):

    _name = "vit.user"
    _description = "vit.user"


    def action_reload(self):
        pass

    Attribute1 = fields.( string=_("Attribute1"))


