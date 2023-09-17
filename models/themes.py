# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Theme(models.Model):
     _name = 'documentarywatchodoo.theme'
     _description = 'Theme for documentary watch'

     label = fields.Char()

     def _get_name(self):
        """ Utility method to allow name_get to be overrided without re-browse the partner """
        theme = self
        name = theme.label or ''

        return name.strip()

     def name_get(self):
        res = []
        for theme in self:
            name = theme._get_name()
            res.append((theme.id, name))
        return res



#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
