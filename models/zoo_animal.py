from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.zoo'
    id = fields.Intiger('ID', required=True)
    continentOrigen = fields.Char('Continent de origen', required=True)
    dataNaix = fields.Date('Data de naixament')
    paisOrigen = fields.Char('Ciutat')
    sexe = fields.Char('Pais')