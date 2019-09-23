from odoo import models,fields,api


class customer(models.Model):
    _name = 'library.customer'
    _description = "This a custumer that rented in the Westors library"
    
    name = fields.Char() #Name of book
    adress = fields.Text()
    emails = fields.Text()
    phone_number = fields.Text()
    other = fields.Text()
    is_an_author = fields.Boolean()

    rental_ids = fields.One2many('library.rented','name_customer_id')


    