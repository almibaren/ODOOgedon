from odoo import models, fields, api

class User(models.Model):
    _name = 'almibaren.worms.user'
    _description = 'Users for Worms'
    _order = 'name'

    realName = fields.Char('Name')
    surname = fields.Char('Surname')
    name = fields.Char('Username', required=True)
    password = fields.Char('Password', required=True)
    email = fields.Char('Email', required=True)
    hats = fields.Many2many('almibaren.worms.hats',string='Gorros')
