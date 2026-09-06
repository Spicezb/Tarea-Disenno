from decimal import Decimal
from .errores import *

def calcular_recargo(dias_restantes: int, tarifa_diaria: Decimal, recargo_por_riesgo: bool):
    if recargo_por_riesgo == True:
        return dias_restantes * tarifa_diaria * 2
    return dias_restantes * tarifa_diaria

def validar_receta(receta):
    if receta.dias <= 0:
        raise RecetaInvalida("Los días deben ser positivos.")

    if receta.dosis_mg <= 0:
        raise RecetaInvalida("La dosis debe ser positiva.")