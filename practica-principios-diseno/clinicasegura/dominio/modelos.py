from dataclasses import dataclass

@dataclass(frozen=True)
class Cedula:
    numCedula: str

    def __init__(self,numCedula):
        self.numCedula=numCedula

@dataclass(frozen=True)
class Receta:
    cedula: Cedula
    folio: int
    dias: int
    dosis: float
    riesgo: bool

    def __init__(self,folio,vigenciaDias,dosis,cedula,riesgo):
        self.folio=folio
        self.vigenciaDias=vigenciaDias
        self.dosis=dosis
        self.cedula=cedula
        self.riesgo = riesgo

@dataclass(frozen=True)
class Despacho:
    receta: Receta
    cadena: str

    def __init__(self,receta,cadena):
        self.receta=receta
        self.cadena=cadena