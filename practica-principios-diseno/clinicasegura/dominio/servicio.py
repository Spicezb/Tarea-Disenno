from .modelos import *
from .reglas import *
from ..aplicacion.configuracion import *
from .puertos import *
from datetime import timedelta, datetime
from .errores import *

class EmisionDeRecetas:
    pasarelas: dict
    folios: GeneradorFolio
    reloj: Reloj
    bitacora: Bitacora

    def __init__(self, folios: GeneradorFolio, reloj:Reloj, bitacora:Bitacora, pasarelas:dict):
        self.folios = folios
        self.reloj = reloj
        self.bitacora = bitacora
        self.pasarelas = pasarelas

    def emitir(self, receta: Receta, cadena: str) -> Despacho:
        validar_receta(receta)
        pasarela = self.pasarelas.get(cadena)
        if pasarela is None:
            raise CadenaNoSoportada(cadena)
        folio = self.folios.siguiente()
        vence = self.reloj.ahora() + timedelta(days=receta.dias)
        try:
            despacho = pasarela.enviar(receta, folio, vence)
        except TimeoutError as e:
            self.bitacora.registrar("error_farmacia", folio)
            raise FarmaciaNoDisponible(cadena) from e
        self.bitacora.registrar("emitida", despacho.folio)
        return despacho