from curso import Curso
from estudiante import Estudiante

curso1 = Curso("Matemáticas", 50, "Profesor A")
curso2 = Curso("Historia", 20, "Profesor B")
curso3 = Curso("Fisica", 30, "Profesor C")


estudiante1 = Estudiante("Juan", 20, 12345)
estudiante2 = Estudiante("Ale", 22, 23456)
estudiante3 = Estudiante("Lola", 21, 34567)
estudiante1.agregar_curso(curso1)
estudiante2.agregar_curso(curso1)
estudiante2.agregar_curso(curso3)
estudiante3.agregar_curso(curso2)
estudiante2.mostrar_info()
estudiante1.mostrar_info()
estudiante3.mostrar_info()
