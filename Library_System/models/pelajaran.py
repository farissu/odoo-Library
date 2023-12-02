from odoo import fields, models, api


class LibraryPelajaran(models.Model):
    _name = 'library.pelajaran'

    name = fields.Char('Mata Pelajaran', required=True)
    guru_ids = fields.Many2many('res.users', domain=[('is_guru', '=', True)], string="Pengajar")
