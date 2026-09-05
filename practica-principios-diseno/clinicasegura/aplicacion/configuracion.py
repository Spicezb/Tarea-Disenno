from dataclasses import dataclass

@dataclass(frozen=True)
class Configuracion:
    vigencia_dias: int
    tarifa_diaria: float
    timeout: float