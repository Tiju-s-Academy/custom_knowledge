# -*- coding: utf-8 -*-
from odoo import models,fields
from random import randint

class KnowledgeTag(models.Model):
    _name = 'knowledge.tag'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string='Color Index', default=_get_default_color)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]
