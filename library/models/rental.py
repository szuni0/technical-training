# -*- coding: utf-8 -*-
from odoo import fields, models


class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')

    book_isbn = fields.Char(string='ISBN', related="book_id.isbn")
    partner_name = fields.Char(related="customer_id.name") 
    partner_email = fields.Char(related="customer_id.email")

    rental_date = fields.Date()
    return_date = fields.Date()
