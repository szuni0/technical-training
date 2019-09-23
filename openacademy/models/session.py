from odoo import models,fields,api


class session(models.Model):
    _name = 'openacademy.session'
    _description = "This is a course of the Westors library"

    name = fields.Char() #Name of course

    start_date = fields.Datetime()
    end_date = fields.Datetime()
    course_id = fields.Many2one('openacademy.course')
    teacher_id = fields.Many2one('openacademy.person')
    attendee_ids = fields.Many2many('openacademy.person')
    room_capacity = fields.Integer()

