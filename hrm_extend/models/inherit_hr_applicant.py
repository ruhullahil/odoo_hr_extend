from odoo import fields, models, api


class InheritHrApplicant(models.Model):
    _inherit = 'hr.applicant'
    _description = 'InheritHrApplicant'

    emergence_contact_ids = fields.One2many('hr.emergency.contact.line', 'applicant_id',
                                            string='Emergency Contacts')
    education_info_ids = fields.Many2many('hr.education.line', string='Education Info')
    assign_manager = fields.Many2one('hr.employee', string='Manager')

    def create_employee_from_applicant(self):
        ending_day_of_current_year = fields.date.today().replace(month=12, day=31)
        # leave_type = self.env['hr.leave.type'].sudo().search(
        #     [('validity_start', '<=', ending_day_of_current_year)], limit=1)
        dict_act_window = super(InheritHrApplicant, self).create_employee_from_applicant()
        dict_act_window['context']['default_education_info'] = self.education_info_ids.ids
        dict_act_window['context']['default_parent_id'] = self.assign_manager.id
        # dict_act_window['context']['default_current_leave_id'] = leave_type.id

        return dict_act_window


class HrEmergencyContactLine(models.Model):
    _name = 'hr.emergency.contact.line'
    _description = 'HrEmergencyContactLine'

    name = fields.Char(string='Name', required=True)
    phone_number = fields.Char(string='Phone', required=True)
    address = fields.Text(string='Address')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    applicant_id = fields.Many2one('hr.applicant', string='Applicant')


class HrEducationLine(models.Model):
    _name = 'hr.education.line'
    _description = 'HrEducationLine'

    @api.model
    def _get_passing_year(self):
        start_year = int(fields.date.today().year) - 30
        year_list = list()
        for i in range(50):
            year = start_year + i
            year_list.append((str(year), str(year)))
        return year_list

    name = fields.Char(string='Institute')
    degree = fields.Many2one('hr.education.degree', string='Degree')
    passing_year = fields.Selection(selection=_get_passing_year, string='Passing Year',
                                    default=str(fields.date.today().year), store=True)


class HrDegree(models.Model):
    _name = 'hr.education.degree'
    _description = 'HrDegree'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
