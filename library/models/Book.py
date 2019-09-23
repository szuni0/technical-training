from odoo import models,fields,api


class book(models.Model):
    _name = 'library.book'
    _description = "This is a book of the Westors library"
    
    name = fields.Char() #Name of book
    author = fields.Many2one('library.customer') 
    Edition = fields.Datetime()
    isbn = fields.Text()
    editor = fields.Text()
    rentals_ids = fields.One2many('library.rented', 'name_book_id')
    