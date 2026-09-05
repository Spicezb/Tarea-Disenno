from typing import Protocol
from datetime import datetime
from .modelos import *

class Pasarela(Protocol):

    def enviar(self, receta:Receta) -> int:
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