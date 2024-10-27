class Materia: 

    def __init__(self,nombrem: str, instructor: str, descripcion: str, semestre: int, creditos: int, id, maestro: Maestro):
        self.nombrem = nombrem
        self.instructor = instructor
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        self.id = id 
        self.maestro = Maestro


    def mostrar_info_materias(self):
        info = f"Instructor: {self.instructor}, Nombre Completo: {self.nombrem}, Descripcion: {self.descripcion}, Semestre: {self.semestre},ID: {self.id}"
        return info