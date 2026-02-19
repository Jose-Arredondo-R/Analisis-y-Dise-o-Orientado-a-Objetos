from typing import List

class Usuario:
    def __init__(self, idUsuario: int, nombre: str, limite_prestamos: str):
        self.__idUsuario = idUsuario
        self.__nombre = nombre
        self.__limite_prestamos = limite_prestamos
        self.__prestamos_activos: List["Prestamo"] = []

    def tiene_cupo(self) -> bool:
        return len(self.__prestamos_activos) < int(self.__limite_prestamos)

    def registrar_prestamo(self, prestamo: "Prestamo") -> None:
        self.__prestamos_activos.append(prestamo)

    def quitar_prestamo(self, prestamo: "Prestamo") -> None:
        if prestamo in self.__prestamos_activos:
            self.__prestamos_activos.remove(prestamo)
