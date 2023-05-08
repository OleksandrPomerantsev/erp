from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    id = fields.Intiger('ID', required=True)
    perill = fields.Boolean('Perill de exincion (1 = si,0 = no)', required=True)
    familia = fields.Char('Familia')
    nomCientific = fields.Char('Nom cientific')
    nomVulgar = fields.Char('Nom vulgar')