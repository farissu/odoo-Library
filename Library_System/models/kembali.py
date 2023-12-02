from odoo import fields, models, api
from datetime import datetime

class Librarykembali(models.Model):
    _name = 'library.kembali'

    Dokumen_kembali = fields.Many2one('library.pinjam', string='Dokumen Pinjam ', required=True)
    Tanggal_kembali = fields.Date(string='Tanggal kembali', default=datetime.today(), required=True)
    Pengelola_pinjam = fields.Many2one('res.partner', string='Peminjam', required=True)
    status = fields.Selection([
        ('rancangan', 'Rancangan'),
        ('Dikembali', 'Dikembali'),
        ('selesai', 'Sudah Kembali')
    ], default="rancangan", required=True)


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
