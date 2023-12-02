from odoo import fields, models, api


class Librarypenerbit(models.Model):
    _name = 'library.penerbit'

    Judul_penerbit = fields.Char(string="Judul buku ",required=True)
    Nama  = fields.Char(string="Nama ", required=True)
    Tahun_terbit = fields.Char(string="Tahun terbit ")