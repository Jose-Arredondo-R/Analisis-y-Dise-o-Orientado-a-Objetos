class Copia:
    def __init__(self, id_copia: str, libro, ubicacion: str):
        self.__id_copia = id_copia
        self.__libro = libro
        self.__ubicacion = ubicacion
        self.__estado = True

    def get_estado(self) -> str:
        return "disponible" if self.__estado else "prestada"

    def prestar(self) -> bool:
        if self.__estado:
            self.__estado = False
            return True
        return False

    def devolver(self) -> None:
        self.__estado = True

