# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartners(models.Model):
    _inherit = 'res.partners'

    name = fields.Char()
    is_tested = fields.Boolean()


class Test(models.Model):
    _name = 'test.test'

    test_name = fields.Char(string='Name')
    test_purpose = fields.Text(string='Purpose')
    tester = fields.Many2one('res.partners', ondelete='set null', string="Tester", index=True)


class TestSession(models.Model):
    _name = 'test_session.test'

    test = fields.Many2one('test.test', ondelete='set null', string='Test', index=True)
    start_date = fields.Date()
    end_date = fields.Date()
    duration = fields.Integer(compute='compute_duration', help="Duration in days")

    @api.depends('start_date', 'end_date')
    def compute_duration(self):
        # Calculate duration between two date and return count of days(integer type).

        for record in self:
            if not (record.start_date and record.end_date):
                    continue

            start_date = fields.Datetime.from_string(record.start_date)
            end_date = fields.Datetime.from_string(record.end_date)
            record.duration = (end_date - start_date).days + 1

