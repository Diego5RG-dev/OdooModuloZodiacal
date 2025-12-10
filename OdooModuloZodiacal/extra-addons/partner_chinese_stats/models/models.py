# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date # Importamos date


class partner_chinese_stats(models.Model):
    _inherit = 'res.partner'

    f_nac = fields.Date("Fecha de nacimiento") 
    edad = fields.Integer(String= "Edad", readonly = True, compute= "_calcular_edad", store = True) 
    signo_chino = fields.Char(String= "Signo chino", readonly = True, compute= "_calcular_chinada", store = True) 
    codigo_socio = fields.Char(string="Código de Socio", help="Ejemplo: VIP-1234")
    nivel_fidelidad = fields.Char(string="Nivel de Fidelidad", readonly=True, compute= "_calcular_nivel_fidelidad", store=True)


    @api.depends('f_nac')
    def _calcular_edad(self):
        today = date.today() 
        for record in self:
            if record.f_nac:
                age = today.year - record.f_nac.year - ((today.month, today.day) < (record.f_nac.month, record.f_nac.day))
                record.edad = age
            else:
                record.edad = 0


    @api.depends('f_nac')
    def _calcular_chinada(self): 
        signos = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", 
                  "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"]
        
        for record in self: 
            if record.f_nac:
                year_offset = record.f_nac.year - 1900
                signo_index = year_offset % 12
                record.signo_chino = signos[signo_index]
            else:
                record.signo_chino = "Sin fecha de nacimiento"
            
    
    @api.depends('codigo_socio')
    def _calcular_nivel_fidelidad(self):
        for record in self:
            codigo = record.codigo_socio
            
            if codigo and codigo.upper().startswith('G'):
                record.nivel_fidelidad = "Gold"

            elif codigo:
                record.nivel_fidelidad = "Premium"

            else:
                record.nivel_fidelidad = "Estándar"