from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    name = fields.Char(compute='_get_name',string="Nom complet",readonly='True',store=False)
    nom = fields.Char('Nom', required=True)
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('Ciutat', required=True)
    pais = fields.Char('Pais', required=True)
    latitud = fields.Float('Latitud', required=True)
    longitud = fields.Float('Longitud', required=True)
    aeroportDesti_ids = fields.One2many('plane.vol','aeroportDesti',String='aeroportDesti')
    aeroportOrigen_ids = fields.One2many('plane.vol','aeroportOrigen',String='aeroportOrigen')
    image = fields.Image(string="Imagen")
    def _get_name(self):
        for record in self:
            record.name = str(record.nom)