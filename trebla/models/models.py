# -*- coding: utf-8 -*-

from odoo import models, fields, api


class player(models.Model):
     _name ='trebla.player'
     _description ='trebla.player'

     name = fields.Char(string = "nom")
     surname = fields.Char(string = "cognoms")
     race =fields.One2many('trebla.race','player')

class race(models.Model):
     _name='trebla.race'
     _description = 'trebla.race'
     name=fields.Char(string="raza")
     player=fields.Many2one("trebla.player")
     armour=fields.Many2many('trebla.armour')


class armour(models.Model):
     _name="trebla.armour"
     _description='trebla.armour'
     name=fields.Char(string="armadura")
     race=fields.Many2many('trebla.race')

