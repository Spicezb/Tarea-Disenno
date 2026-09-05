def calcular_recargo(dias_restantes: int, tarifa_diaria: float, recargo_por_riesgo: bool):
    if recargo_por_riesgo == True:
        return dias_restantes * tarifa_diaria * 2
    return dias_restantes * tarifa_diaria

