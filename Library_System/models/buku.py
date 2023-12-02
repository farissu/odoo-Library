from odoo import fields, models, api


class Librarybuku(models.Model):
    _name = 'library.buku'

    No_Inventaris  = fields.Char(string="No Inventaris ", required=True)
    Judul_buku = fields.Char(string="Judul buku ",required=True)
    Penulis = fields.Many2many('library.penulis', string='Penulis')
    Tahun_terbit = fields.Char(string="Tahun terbit ")
    Penerbit = fields.Many2one('library.penerbit', string='Penerbit')
    ISBN = fields.Char(string="ISBN ")
