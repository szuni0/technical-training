from odoo import models,fields,api


class Course(models.Model):
    _name = 'openacademy.Course'
    _description = "This is a course of the Westors library"

    name = fields.char() #Name of course
    _description = fields.text()
    level = fields.session([('1','First grade'), ('2','second grade'), ('3', 'Third grade')])
    responsable_id = fields.Many2one('openacademy.person')
    session_ids = fields.One2many('openacademy.session', 'course


