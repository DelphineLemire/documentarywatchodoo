# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Topic(models.Model):
     _name = 'documentarywatchodoo.topic'
     _description = 'Topic for documentary watch'

     name = fields.Char()
     description = fields.Text()
     theme_id = fields.Many2one('documentarywatchodoo.theme', 
                           string='Theme'
                           )
     def _get_name(self):
        """ Utility method to allow name_get to be overrided without re-browse the partner """
        topic = self
        name = topic.name or ''

        return name.strip()

     def name_get(self):
        res = []
        for topic in self:
            name = topic._get_name()
            res.append((topic.id, name))
        return res

class Contribution(models.Model):
     _name = 'documentarywatchodoo.contribution'
     _inherit = ['mail.thread.cc',
                'mail.activity.mixin',
                'utm.mixin',
               ]
     _description = 'Contribution for documentary watch'

     name = fields.Char()
     url = fields.Char()

     contributor_id =  fields.Many2one('res.partner', 
                           string='Contributor'
                           )
     topic_id = fields.Many2one('documentarywatchodoo.topic', 
                           string='Topic'
                           )
     def _get_name(self):
        """ Utility method to allow name_get to be overrided without re-browse the partner """
        contribution = self
        name = contribution.name or ''

        return name.strip()

     def name_get(self):
        res = []
        for contribution in self:
            name = contribution._get_name()
            res.append((contribution.id, name))
        return res


#partner_id = fields.Many2one(
#        'res.partner', string='Customer', check_company=True, index=True, tracking=10,
#        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
#        help="Linked partner (optional). Usually created when converting the lead. You can find a partner by its Name, TIN, Email or Internal Reference.")

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
