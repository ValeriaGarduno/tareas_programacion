class Estudiante:
    nombre = ""
    edad = 0
    id = 0 
    cursos = []

    def __init__(self, nombre, edad, id):
        self.nombre = nombre
        self.edad = edad 
        self.id = id
        self.cursos = []
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_info(self):
        print("\n----- Información del Estudiante -----")
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("ID: ", self.id)
        print("\n----- Cursos Registrados -----")
        for curso in self.cursos:
            print(f"\nNombre del curso: {curso.nombre_curso}")
            print(f"Instructor: {curso.instructor}")
            print(f"codigo Curso: {curso.codigo_curso}")
