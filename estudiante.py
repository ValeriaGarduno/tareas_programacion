class Estudiante:
    nombre = ""
    edad = 0
    id = 0 
    cursos = []

    def __init__(self, nombre, edad, curso, id):
        self.nombre = nombre
        self.edad = edad 
        self.id = id
        self.cursos = curso
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_info(self):
        print("\n----- Cursos Registrados -----")

        print("Nombre: ", self.nombre)
        
        for curso in self.cursos:
            print("\n")
            print("Id: ", curso.nombre_curso)
            print("instructor", curso.instructor)
