from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    id = fields.Integer('ID', required=True)
    nom = fields.Char('Nom', required=True)
    grandaria = fields.Char('Tamaño')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')