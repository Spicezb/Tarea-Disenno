from typing import Protocol
from datetime import datetime
from .modelos import *

class Pasarela(Protocol):
    cadena: str

    def enviar(self, receta:Receta, folio:str, vence:datetime) -> Despacho:
        ...

class Reloj(Protocol):

    def ahora(self) -> datetime:
        ...
class GeneradorFolio(Protocol):

    def siguiente(self) -> str:
        ...

class Bitacora(Protocol):

    def registrar(self,folio:str,evento:str,cuando:datetime) -> None:
        ...