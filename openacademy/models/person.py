from odoo import models,fields,api


class Person(models.Model):
    _name = 'openacademy.Person'
    _description = "This is a course of the Westors library"

    name = fields.char() #Name of person

    is_teacher = fields.Boolean()

    session_ids = fields.Many2many('openacademy.session')


