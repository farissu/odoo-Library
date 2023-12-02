from odoo import fields, models, api
from datetime import datetime

class LibraryPinjam(models.Model):
    _name = 'library.pinjam'

    Anggota_pinjam = fields.Many2one('res.partner', string='Peminjam', required=True)
    Buku_pinjam = fields.Many2one('library.buku', string='Buku Pinjaman', required=True)
    Tanggal_pinjam = fields.Date(string='Tanggal pinjam', default=datetime.today(), required=True)
    Batas_pinjam = fields.Date('Batas peminjaman', required=True)
    status = fields.Selection([
        ('rancangan', 'Rancangan'),
        ('Dipinjam', 'Dipinjam'),
        ('selesai', 'Sudah Kembali')
    ], default="rancangan", required=True)

    def Dipinjam_button(self):
        self.status = 'Dipinjam'

    def selesai_button(self):
        self.status = 'selesai'

class SchoolAnggota(models.Model):
    _inherit = 'res.partner'

    is_murid = fields.Boolean(string="Murid", required=True)
    nis = fields.Char(string="NIS", required=True)
    age = fields.Integer(string="Umur", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender", required=True)
    kelas_id = fields.Many2one(string="Kelas", comodel_name="your_class_model_name", required=True)
