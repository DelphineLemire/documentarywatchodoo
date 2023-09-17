# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    contribution_ids = fields.One2many('documentarywatchodoo.contribution', 'contributor_id', string='Contributions')
    contribution_count = fields.Integer("Contribution", compute='_compute_contribution_count')

    
    def _compute_contribution_count(self):
        # retrieve all children partners and prefetch 'parent_id' on them
        all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        all_partners.read(['parent_id'])

        contribution_data = self.env['documentarywatchodoo.contribution'].with_context(active_test=False)._read_group(
            domain=[('contributor_id', 'in', all_partners.ids)],
            fields=['contributor_id'], groupby=['contributor_id']
        )

        self.contribution_count = 0
        for group in contribution_data:
            partner = self.browse(group['contributor_id'][0])
            while partner:
                if partner in self:
                    partner.contribution_count += group['contributor_id_count']
                partner = partner.parent_id

    def action_view_contribution(self):
        '''
        This function returns an action that displays the contributions from partner.
        '''
        action = self.env['ir.actions.act_window']._for_xml_id('documentarywatchodoo.action_window_contribution')
        action['context'] = {'active_test': False}
        if self.is_company:
            action['domain'] = [('contributor_id.commercial_partner_id', '=', self.id)]
        else:
            action['domain'] = [('contributor_id', '=', self.id)]
        return action
