from curso import Curso
from estudiante import Estudiante

while True:
    print("\n*** BIENVENIDO ***")
    print("Opciones en el Sistema")
    print("1. Registrar Curso")
    print("2. Mostrar Cursos")
    print("3. Salir")

    opcion = input("Ingresa la opción que deseas: ")

    if opcion == "1":
        id = int(input("Ingresa el id del estudiante: "))
        if id == "1234":
            curso = Curso("Progra 1", 1, "Javier")
            estudiante_uno.agregar_curso(curso)

        elif id== "2345":
            curso = Curso("Dibujo", 2, "Ponciano")
            estudiante_dos.agregar_curso(curso)
            
        estudiante_dos = Estudiante(nombre="Alejandra", edad=22, cursos=curso, id=2345)
        estudiante_uno = Estudiante(nombre="Roberto", edad=20, cursos=curso, id=1234)
        print("\n Curso agregado correctamente")
    
    elif opcion == "2":
        estudiante_uno.mostrar_info()
        estudiante_dos.mostrar_info()
    
    elif opcion == "3":
        print("\nHasta luego")
        break