from escuela.escuela import Escuela
from estudiantes.estudiantes import Estudiante
from datetime import datetime
from maestros.maestros import Maestro
from materias.materias import Materia

escuela = Escuela()

while True:
    print("*** MINDBOX ***")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestros") 
    print("8. Mostrar materias")
    print("9. Mostrar grupos")
    print("10. Eliminar estudiante")
    print("11. Eliminar maestro")
    print("12. Eliminar materia")
    print("13. Salir")
    
    
    opcion = input("Ingresa una opcion para continuar: ")
    
    if opcion == "1":
        print("Seleccionaste la opcion de registrar")
        
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa el curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        numero_control = escuela.generar_numero_control()
        
        estudiante = Estudiante(nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, numero_control=numero_control)
        escuela.registrar_estudiante(estudiante)
        print(numero_control)
        print(f"estudiante registrado correctamente {nombre}")

    
    elif opcion == "2":
        print("Seleccionaste la opcion registrar maestro")
        nombre = input("Ingresa nombre del maestro")
        apellido = input("Ingresa apellido del maestro")
        rfc = input("Ingresa rfc del maestro")
        sueldo = int(input("Ingresa sueldo del maestro"))
        
        numero_control_maestro = escuela.generar_numero_control_maestro(nombre,rfc)
        print(numero_control_maestro)
        
        maestro = Maestro(nombre,apellido, rfc, sueldo)
        escuela.registrar_maestro(maestro)
    
    elif opcion == "3":
        nombrem = input("Ingresa rnombre de la materia")
        semestre = int(input("Ingresa no. semestre que la cursa"))
        instructor = input("Ingresa instructor de la materia")
        creditos = int(input("Ingresa no. creditos de la materia"))
        descripcion = input("Ingresa descripcion de la materia")
        id = escuela.generar_id_materia(nombrem, semestre, creditos)
        print(id)
        
        materia = Materia(nombrem, instructor, descripcion, semestre, creditos)
        escuela.registrar_materia(materia)
    elif opcion == "4":
        pass
    
    elif opcion == "5":
        pass

    elif opcion == "6":
        escuela.listar_estudiantes()
        
    elif opcion == "7":
        escuela.listar_maestros()
    
    elif opcion == "8":
        escuela.listar_materia()

    elif opcion == "10":
        print("eleccionaste la opcion eliminar estudiante")
        numero_control = input("ingresa el no. control")
        escuela.eliminar_estudiante(numero_control=numero_control)

    elif opcion == "11":
        print("eleccionaste la opcion eliminar maestro")
        numero_control_maestro = input("ingresa el no. control")
        escuela.eliminar_maestro(numero_control_maestro=numero_control_maestro)
    
    elif opcion == "12":
        print("eleccionaste la opcion eliminar materia")
        id = input("ingresa el id")
        escuela.eliminar_materia(id=id)

    elif opcion == "13":
        print("Hasta luego")
        break
    