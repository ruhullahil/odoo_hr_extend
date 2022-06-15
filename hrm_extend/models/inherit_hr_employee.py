from odoo import fields, models, api
from odoo.exceptions import ValidationError


class InheritHrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'InheritHrEmployee'

    education_info = fields.Many2many('hr.education.line', string='Education Info')
    emergence_contact_ids = fields.One2many('hr.emergency.contact.line', 'employee_id',
                                            string='Emergency Contacts')

    @api.model
    def create(self, values):
        # Add code here
        res = super(InheritHrEmployee, self).create(values)
        ending_day_of_current_year = fields.date.today().replace(month=12, day=31)
        # ('validity_start', '>=', fields.date.today()),
        leave_type = self.env['hr.leave.type'].sudo().search(
            [('validity_start', '<=', ending_day_of_current_year)],
            limit=1)
        holiday_allowcation = {
            'name': 'holiday of paid',
            'holiday_status_id': leave_type.id,
            'allocation_type': 'regular',
            'number_of_days_display': 20,
            'number_of_days': 20,
            'holiday_type': 'employee',
            'employee_id': res.id
        }
        holiday = self.env['hr.leave.allocation'].sudo().create(holiday_allowcation)
        if holiday:
            holiday.sudo().action_validate()
        else:
            raise ValidationError('Some thing went wrong !! leave allocation not created!!')

        for rec in res.applicant_id:
            for contact in rec.emergence_contact_ids:
                contact.sudo().write({'employee_id': res.id})
        return res
