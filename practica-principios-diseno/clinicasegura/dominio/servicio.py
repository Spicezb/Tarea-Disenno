from .modelos import *
from .reglas import *
from ..aplicacion.configuracion import *
from .puertos import GeneradorFolio,Reloj
from datetime import timedelta, datetime

class EmisionDeRecetas:
    config: Configuracion
    generadorFolio: GeneradorFolio
    reloj: Reloj

    def __init__(self, config: Configuracion, generadorFolio: GeneradorFolio, reloj:Reloj):
        self.config = config
        self.generadorFolio = generadorFolio
        self.reloj = reloj

    def emitir(self, receta: Receta) -> Despacho:
        pass
        #recargo = calcular_recargo(receta.dias,self.config.tarifa_diaria,receta.riesgo)
        #folio = self.generadorFolio.siguiente()
        #vence = self.reloj.ahora() + timedelta(days=self.config.vigencia_dias)
        #return Despacho(folio,,vence) #se podrá resorlver cuando se obtenga la cadena mediante la pasarela