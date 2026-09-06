from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass(frozen=True)
class Cedula:
    numCedula: str

@dataclass(frozen=True)
class Receta:
    cedula: Cedula
    dias: int
    dosis_mg: float
    medicamento:str
    riesgo: bool = False

@dataclass(frozen=True)
class Despacho:
    folio: str
    cadena: str
    vence: datetime
