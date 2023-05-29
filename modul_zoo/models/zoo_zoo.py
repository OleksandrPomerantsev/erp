from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    name = fields.Char(compute='_get_name',string="Nom complet",readonly='True',store=False)
    nom = fields.Char('Nom', required=True)
    grandaria = fields.Char('Tamaño')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    animals_ids = fields.One2many('zoo.animal','zoo_id',String='Animals')
    image = fields.Binary(string="Imagen")
    def _get_name(self):
        for record in self:
            record.name = str(record.nom)