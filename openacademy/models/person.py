from odoo import models,fields,api


class Person(models.Model):
    _name = 'openacademy.person'
    _description = "This is a course of the Westors library"

    name = fields.Char() #Name of person

    is_teacher = fields.Boolean()

    session_ids = fields.Many2many('openacademy.session')


