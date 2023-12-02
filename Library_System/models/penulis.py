from odoo import fields, models, api


class Librarypenulis(models.Model):
    _name = 'library.penulis'

    Judul_penulis = fields.Char(string="Judul buku ",required=True)
    Nama  = fields.Char(string="Nama ", required=True)
    Tahun_terbit = fields.Char(string="Tahun terbit ")