from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    rfc: str
    ano_antiguedad: datetime
    
    def __init__(self, numero_control, nombre: str, apellido: str, curp: str, ano_antiguedad: datetime, contrasenia: str, rol: Rol):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.COORDINADOR)
        self.curp = curp
        self.ano_antiguedad = ano_antiguedad
        
    def mostrar_info_coordinador(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.numero_control}, Nombre Completo: {nombre_completo}, Curp: {self.curp}, AñO ANTIGUEDAD: {self.ano_antiguedad}, ROL: {self.rol.value}"
        return info