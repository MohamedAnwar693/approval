from odoo import fields, models, api, _


class ApprovalApproval(models.Model):
    _name = "approval.approval"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "APPROVAL"

    approval_subject = fields.Char(string='Approval Subject', required=True, tracking=True)
    request_owner = fields.Char(string='Request Owner', required=True, tracking=True)
    category = fields.Char(string='Category', required=True, tracking=True)
    date = fields.Date(string="Date")
    from_period = fields.Date(string='From')
    to_period = fields.Date(string='To')
    period = fields.Char(string='Period', store=True)
    location = fields.Char(string='Location', required=True, tracking=True)
    contact = fields.Char(string='Contact', required=True, tracking=True)
    amount = fields.Float(string='Amount', required=True, tracking=True)
    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    state = fields.Selection([('to_submit', 'TO SUBMIT'), ('submitted', 'SUBMITTED'),
                              ('approved', 'APPROVED'), ('refused', 'REFUSED'), ('cancel', 'CANCEL')],
                             default='to_submit',
                             string="Status", tracking=True)

    def action_to_submit(self):
        for rec in self:
            rec.state = 'to_submit'

    def action_submitted(self):
        for rec in self:
            rec.state = 'submitted'

    def action_approved(self):
        for rec in self:
            rec.state = 'approved'

    def action_refused(self):
        for rec in self:
            rec.state = 'refused'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.depends('From', 'To')
    def _compute_period(self):
        for record in self:
            if record.from_period and record.to_period:
                record.period = f"{record.from_period.strftime('%Y-%m-%d')} to {record.to_period.strftime('%Y-%m-%d')}"
            else:
                record.period = False

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('approval.approval') or _('New')
        res = super(ApprovalApproval, self).create(vals)
        return res
