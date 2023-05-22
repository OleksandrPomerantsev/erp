from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    name = fields.Char(compute='_get_name',string="Nom complet",readonly='True',store=False)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca', required=True)
    model = fields.Char('Model', required=True)
    maxVel = fields.Float('maxVelocitat')
    vol_ids = fields.One2many('plane.vol','avio_id',String='Avio')
    def _get_name(self):
        for record in self:
            record.name = str(record.marca) + " " + str(record.model)