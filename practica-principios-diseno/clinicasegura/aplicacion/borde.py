import re
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field, field_validator
from clinicasegura.dominio.modelos import Cedula, Receta

def validar_cedula(cedula):
    if re.match(r"^\d-\d{4}-\d{4}$",cedula):
        return True
    return False

class SolicitudReceta(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )

    cedula: str
    medicamento: str
    dias: int = Field(gt=0, le=90)
    dosis_mg: Decimal = Field(gt=0)
    riesgo: bool = False

    @field_validator("cedula")
    @classmethod
    def cedula_valida(cls, valor):
        if not validar_cedula(valor):
            raise ValueError("La cédula tiene formato 0-0000-0000.")
        return valor

def a_receta(solicitud: SolicitudReceta) -> Receta:
    return Receta(
        cedula=Cedula(solicitud.cedula),
        medicamento=solicitud.medicamento,
        dias=solicitud.dias,
        dosis_mg=solicitud.dosis_mg,
        riesgo=solicitud.riesgo,
    )