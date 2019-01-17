from odoo import models, fields, api

class Hats(models.Model):
    _name = 'almibaren.worms.hats'
    _description = 'Hats for Worms'
    _order = 'date_release desc'

    short_name = fields.Char('Titulo corto', size=20, translate=False)
    name = fields.Char('Nombre', required=True)
    date_release = fields.Date('Release Date')
    description = fields.Html('Descripcion', sanitize=True, strip_style = True, translate = False)
    prize = fields.Float('Precio',(3,1))
    cover = fields.Binary('Imagen')
    rating = fields.Float('Valoración', (3, 1))
