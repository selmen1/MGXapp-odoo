from odoo import api, fields, models


class Demand(models.Model):
    _name = 'mgx.order'
    _description = "MGX demand"

    name = fields.Char(string='Object', required=True, translate=True)
    status = fields.Selection([
        ('demand', 'Demand'),
        ('verification', 'Verification'),
        ('confirmation', 'Confirmation'),], required=True, default='demand',)
    note = fields.Text(string='Description')
    employee_mgx_id = fields.Many2one('hr.employee', string='MGX Employee')
    article_mgx_id = fields.Many2one('product.template', string='MGX Article')
    quantity = fields.Integer('quantity of items')



