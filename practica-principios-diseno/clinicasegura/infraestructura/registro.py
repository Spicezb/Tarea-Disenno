def construir_registro(pasarelas):
    registro = {}
    for pasarela in pasarelas:
        registro[pasarela.cadena]=pasarela
    return registro