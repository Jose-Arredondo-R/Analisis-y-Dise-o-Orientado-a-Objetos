from Copia import Copia

class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__copias = []

    def agregar_copia(self, id_copia: str, ubicacion: str):
        nueva_copia = Copia(id_copia, self, ubicacion)
        self.__copias.append(nueva_copia)
        return nueva_copia

    def obtener_disponibles(self):
        return [c for c in self.__copias if c.get_estado() == "disponible"]
