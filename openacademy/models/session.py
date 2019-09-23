from odoo import models,fields,api


class session(models.Model):
    _name = 'openacademy.Course'
    _description = "This is a course of the Westors library"

    name = fields.char() #Name of course

    start_date = fields.Datetime()
    end_date = fields.Datetime()
    course_id = fields.many2one()
    teacher_id = fields.many2one(openacademy.person)
    attendee_ids = fields.many2many('openacademy.person')
    room_capacity = fields.Integer()

