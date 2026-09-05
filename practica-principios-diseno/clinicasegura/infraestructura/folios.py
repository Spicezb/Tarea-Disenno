import uuid

class GeneradorFolioUUID:

    def siguiente(self) -> str:
        return str(uuid.uuid4())