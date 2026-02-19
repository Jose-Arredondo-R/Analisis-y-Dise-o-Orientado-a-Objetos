from datetime import datetime
from Copia import Copia
from Usuario import Usuario


class Prestamo:
    def __init__(self, copia: Copia, usuario: Usuario, fecha_vencimiento :datetime):
        self.__copia = copia
        self.__usuario = usuario
        self.fecha_inicio = datetime.now()
        self.fecha_vencimiento = fecha_vencimiento
        self.fecha_de_devolucion = None

@property
def copia(self):
    return self.__copia

@property
def usuario(self) -> Usuario:
    return self.__usuario

def ejectar_prestamo(self) -> bool:
    if not self.usuario.tiene_cupo(self):
        return False 
    if not self.__copia.prestar(self):
        return False
    
    self.__usuario.regristrar_prestamo(self)
    return True
def finalisar_devoluciones(self) ->None:
    self.__fecha_de_devolucion = datetime.now()
    self.__copia.devolver()
    self.__ususario.quitar_prestamo(self)
