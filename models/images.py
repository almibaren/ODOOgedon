from odoo import models, fields, api

class Images(models.Model):
    _name = 'almibaren.worms.images'

    name = fields.Char('Nombre', required=True)
    path = fields.Char('Ruta', required=True)
    cover = fields.Binary('Imagen')
