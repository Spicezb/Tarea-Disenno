from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Configuracion:
    vigencia_dias: int
    tarifa_diaria: Decimal
    timeout: float