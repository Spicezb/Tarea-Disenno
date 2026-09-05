from .modelos import *
from .reglas import *
from ..aplicacion.configuracion import *

class EmisionDeRecetas:
    config: Configuracion

    def __init__(self, config: Configuracion):
        self.config = config

    def emitir(self, receta: Receta):
        recargo = calcular_recargo(receta.dias,self.config.tarifa_diaria,receta.riesgo)
        return recargo