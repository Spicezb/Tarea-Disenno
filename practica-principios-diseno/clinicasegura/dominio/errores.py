class ErrorDominio(Exception):
    msj: str

    def __init__(self,msj):
        self.msj = msj
        super().__init__(self,msj)

class RecetaInvalida(ErrorDominio):

    def __init__(self,msj="La receta es inválida."):
        super().__init__(msj)

class CadenaNoSoportada(ErrorDominio):
    cadena: str
    
    def __init__(self,cadena):
        self.cadena = cadena
        super().__init__(f"La cadena {cadena} no es soportada.")

class FarmaciaNoDisponible(ErrorDominio):
    farmacia: str

    def __init__(self,farmacia):
        self.farmacia = farmacia
        super().__init__(f"La farmacia {farmacia} no está disponible.")