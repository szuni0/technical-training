from odoo import models,fields,api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = "This is a course of the Westors library"

    name = fields.Char() #Name of course
    description = fields.Text()
    level = fields.Selection([('1','First grade'), ('2','second grade'), ('3', 'Third grade')])
    responsable_id = fields.Many2one('openacademy.person')
    session_ids = fields.One2many('openacademy.session', 'course_id')


