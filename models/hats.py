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
    cover = fields.Many2many('almibaren.worms.images',String="Imagen")
    rating = fields.Float('Valoración', (3, 1))
    sales = fields.Integer(String='Total ventas',compute='_get_total_sales2',store=True)
    #sql = fields.Char(String="SQL", compute = '_get_consulta')
    user_ids = fields.Many2many('almibaren.worms.user', string="Usuario", relation="almibaren_worms_hats_almibaren_worms_user_rel")

    @api.model
    def _get_total_sales(self):
        self.sales = self._cr.execute("SELECT COUNT(almibaren_worms_hats.name) FROM public.almibaren_worms_hats_almibaren_worms_user_rel, public.almibaren_worms_hats WHERE almibaren_worms_hats_almibaren_worms_user_rel.almibaren_worms_hats_id = almibaren_worms_hats.id AND almibaren_worms_hats.name='" + self.name +"'");
        return self.sales;

    @api.depends('user_ids')
    def _get_total_sales2(self):
        for r in self:
            r.sales = len(r.user_ids)
