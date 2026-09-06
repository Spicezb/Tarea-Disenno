from datetime import datetime
from decimal import Decimal
import pytest
from clinicasegura.dominio.modelos import Cedula, Receta
from clinicasegura.dominio.servicio import EmisionDeRecetas
from clinicasegura.dominio.errores import *

class RelojFijo:
    def ahora(self):
        return datetime(2026, 3, 1, 9, 0, 0)

class PasarelaFalsa:
    cadena = "farmauno"

    def enviar(self, receta, folio, vence):
        from clinicasegura.dominio.modelos import Despacho
        return Despacho(folio, self.cadena, vence)

class FoliosFijos:
    def siguiente(self):
        return "F-00001"

class BitacoraFalsa:
    def registrar(self, evento, folio):
        pass

def test_vigencia_con_reloj_fijo():
    servicio = EmisionDeRecetas(
        pasarelas={"farmauno": PasarelaFalsa()},
        reloj=RelojFijo(),
        folios=FoliosFijos(),
        bitacora=BitacoraFalsa(),
    )

    receta = Receta(
        cedula=Cedula("1-1234-5678"),
        medicamento="N02BE01",
        dias=30,
        dosis_mg=Decimal("500"),
    )

    despacho = servicio.emitir(receta, "farmauno")

    assert despacho.vence == datetime(2026, 3, 31, 9, 0, 0)

class PasarelaCaida:
    cadena = "farmauno"

    def enviar(self, receta, folio, vence):
        raise TimeoutError("La farmacia no responde")

def test_cadena_caida():
    servicio = EmisionDeRecetas(
        pasarelas={"farmauno": PasarelaCaida()},
        reloj=RelojFijo(),
        folios=FoliosFijos(),
        bitacora=BitacoraFalsa(),
    )

    receta = Receta(
        cedula=Cedula("1-1234-5678"),
        medicamento="N02BE01",
        dias=30,
        dosis_mg=Decimal("500"),
    )

    with pytest.raises(TimeoutError):
        servicio.emitir(receta, "farmauno")

def test_receta_invalida():
    servicio = EmisionDeRecetas(
        pasarelas={"farmauno": PasarelaFalsa()},
        reloj=RelojFijo(),
        folios=FoliosFijos(),
        bitacora=BitacoraFalsa(),
    )

    receta = Receta(
        cedula=Cedula("1-1234-5678"),
        medicamento="N02BE01",
        dias=0,
        dosis_mg=Decimal("500"),
    )

    with pytest.raises(RecetaInvalida):
        servicio.emitir(receta, "farmauno")