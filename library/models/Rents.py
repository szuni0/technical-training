from odoo import models,fields,api


class rented(models.Model):
    _name = 'library.rented'
    _description = "This a rental order of the Westors library"
    
    name_book_id = fields.Many2one('library.book')
    name_custumer_id = fields.Many2one('library.customer')
    