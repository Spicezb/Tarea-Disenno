from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Cedula:
    numCedula: str

    def __init__(self,numCedula):
        self.numCedula=numCedula

@dataclass(frozen=True)
class Receta:
    cedula: Cedula
    dias: int
    dosis: float
    riesgo: bool

    def __init__(self,vigenciaDias,dosis,cedula,riesgo):
        self.vigenciaDias=vigenciaDias
        self.dosis=dosis
        self.cedula=cedula
        self.riesgo = riesgo

@dataclass(frozen=True)
class Despacho:
    folio: str
    cadena: str
    vence: datetime

    def __init__(self,folio,cadena,vence):
        self.folio=folio
        self.cadena=cadena
        self.vence=vence