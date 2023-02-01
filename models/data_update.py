# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons.base.models.ir_model import FIELD_TYPES

class DataUpdateProcess(models.Model):
    _name = "data.update.process"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Title',required=True)
    description = fields.Html(string='Description')
    requested_by = fields.Many2one('res.partner',string='Requested by',required=True)
    line_ids = fields.One2many('data.update.log','parent_id')
    line_ids_count = fields.Integer(compute='_compute_line_ids')


    @api.depends('line_ids')
    def _compute_line_ids(self):
        for each in self:
            each.line_ids_count = len(each.line_ids)


    def open_line_ids(self):
        domain = [('parent_id', 'in', self.ids)]
        return {
            'name': _('Update details'),
            'view_mode': 'tree,form',
            'views': [(self.env.ref('data_correction_log.data_update_log_view_tree').id, 'tree'),
                      (self.env.ref('data_correction_log.data_update_log_view_form').id, 'form')],
            'res_model': 'data.update.log',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': domain,
        }




class DataUpdateLog(models.Model):
    _name = "data.update.log"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    parent_id = fields.Many2one('data.update.process')
    name = fields.Char(string='Reference',required=True)
    model = fields.Char(string='Model',required=True)
    res_id = fields.Integer(string='Record ID',required=True,help="The ID of the updated record")
    field = fields.Char(string='Field Name',required=True)
    ttype = fields.Selection(selection=FIELD_TYPES, string='Field Type', required=True)
    original_data = fields.Char(string='Original data',required=True)
    new_data = fields.Char(string='New data',required=True)

