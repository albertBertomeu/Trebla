# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class player(models.Model):
    _name = 'trebla.player'
    _description = 'trebla.player'

    name = fields.Char(string="Nom", required=True)
    surname = fields.Char(string="Cognoms")
    birth_year = fields.Integer()
    level=fields.Integer()
    clan = fields.Selection([('1', 'horda'), ('2', 'alianza')])
    race_id = fields.Many2one("trebla.race", domain="[('clan','=',clan)]", ondelete="set null")
    last_login = fields.Datetime(string="última modificació",default=lambda self: fields.Datetime.now())
    atac_total = fields.Integer(default="0", compute='_compute_atac_total')
    defensa_total = fields.Integer(default="0", compute='_compute_defensa_total')
    photo = fields.Image(max_width=200, max_height=200)
    armour = fields.Many2many(comodel_name='trebla.armour',
                              relation="armour_player",
                              column2="armour_id",
                              column1="player_id")



    @api.onchange('level')
    def _onchange_level(self):
        if self.level > 4:
            return {
                'warning': {'title': 'canvi de ámbit', 'message': ' ara ja pots fer duels', 'type': 'notification'}}


    @api.constrains('birth_year')
    def _check_byear(self):
        for s in self:
            if s.birth_year < 2006:
                print('pots jugar')
            else:
               raise ValidationError('no tens prou edat per a jugar')

    def _compute_atac_total(self):
        for player in self:
            total_atac = 0
            for armour in player.armour:
                total_atac += armour.atac
                player.atac_total = total_atac

    def _compute_defensa_total(self):
        for player in self:
            total_defensa = 0
            for armour in player.armour:
                total_defensa += armour.defensa
                player.defensa_total = total_defensa

    def add_level(self):
        for s in self:
            level = s.level + 1
            s.write({'level': level})


class race(models.Model):
    _name = 'trebla.race'
    _description = 'trebla.race'
    name = fields.Char(string="raza")
    description = fields.Text()
    clan = fields.Selection([('1', 'horda'), ('2', 'alianza')])

    player = fields.One2many(comodel_name='trebla.player', inverse_name='race_id')


class armour(models.Model):
    _name = "trebla.armour"
    _description = 'trebla.armour'

    name = fields.Char(string="Armadura")
    is_used = fields.Boolean(string="en uso",default=False)

    player = fields.Many2many(comodel_name='trebla.player',
                              relation="armour_player",
                              column1="armour_id",
                              column2="player_id")
    atac = fields.Integer(default=0)
    defensa = fields.Integer(default=0)
