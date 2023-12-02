from odoo import fields, models, api


class LibraryKelas(models.Model):
    _name = 'library.kelas'

    name = fields.Char(string="Kelas", required=True)
    gedung_id = fields.Many2one(string="Gedung", comodel_name="library.gedung")
    guru_id = fields.Many2one(string="Wali Kelas", comodel_name="res.users", domain=[('is_guru', '=', True)])
    murid_ids = fields.One2many(comodel_name="res.partner", inverse_name="kelas_id", string="Murid",
                                domain=[('is_murid', '=', True)])
    pelajaran_id = fields.Many2one(string="Pelajaran", comodel_name="library.pelajaran")

