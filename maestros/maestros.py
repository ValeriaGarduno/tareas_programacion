from usuario.usuario import Usuario
from usuario.utils.roles import Rol
 
class Maestro(Usuario):
    rfc: str
    sueldo: float

    
    def __init__(self,nombre: str, apellido: str, rfc: str, sueldo: float, numero_control: str, contrasenia: str, rol: Rol):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.ESTUDIANTE)
        self.rfc = rfc
        self.sueldo = sueldo



    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"  
        info = f"RFC: {self.rfc}, Nombre Completo: {nombre_completo}, Sueldo: {self.sueldo}, ID: {self.numero_control}, ROL: {self.rol.value}"
        return info