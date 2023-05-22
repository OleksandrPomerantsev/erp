from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    name = fields.Char(compute='_get_name',string="Nom complet",readonly='True',store=False)
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.Datetime('DataSortida')
    dataArrivada = fields.Datetime('DataArrivada')
    avioDesti = fields.Many2one('plane.aeroport',String='avioDesti')
    avioOrigen = fields.Many2one('plane.aeroport',String='avioOrigen')
    pilot_id = fields.Many2one('plane.pilot',String='Pilot')
    avio_id = fields.Many2one('plane.avio',String='Avio')
    def _get_name(self):
        for record in self:
            record.name = str(record.id)