import re

def validar_cedula(cedula):
    if re.match(r"^\d-\d{4}-\d{4}$",cedula):
        return True
    return False