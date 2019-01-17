from odoo import models, fields, api

class User(models.Model):
    _name = 'almibaren.worms.user'
    _description = 'Users for Worms'
    _order = 'name'

    name = fields.Char('Username', required=True)
    password = fields.Char('Password', required=True)
    realName = fields.Char('Name')
    surname = fields.Char('Surname')
    email = fields.Char('Email', required=True)
    username = fields.Char('Username', required=True)
