import os
from datetime import datetime
from .dominio.servicio import EmisionDeRecetas
from .infraestructura.folios import GeneradorFolioUUID

class RelojSistema:
    def ahora(self) -> datetime:
        return datetime.now()

class BitacoraSimple:
    def registrar(self, folio, evento, cuando):
        pass

class PasarelaSimple:
    cadena = "farmauno"

    def enviar(self, receta, folio, vence):
        from .dominio.modelos import Despacho
        return Despacho(
            folio=folio,
            cadena=self.cadena,
            vence=vence,
        )

def construir_servicio():
    timeout_ms = int(os.environ.get("FARMACIA_TIMEOUT_MS", "1500"))

    pasarela = PasarelaSimple()

    return EmisionDeRecetas(
        pasarelas={pasarela.cadena: pasarela},
        reloj=RelojSistema(),
        folios=GeneradorFolioUUID(),
        bitacora=BitacoraSimple(),
    )