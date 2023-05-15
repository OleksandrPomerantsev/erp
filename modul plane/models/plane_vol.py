from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    name = fields.Char(compute='_get_name',string="Nom complet",readonly='True',store=False)
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.Datetime('DataSortida')
    dataArrivada = fields.Datetime('DataArrivada')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + " " + str(record.cognom)