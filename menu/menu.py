from escuela.escuela import Escuela
from estudiantes.estudiantes import Estudiante
from materias.materias import Materia
from semestre.semestre import Semestre
from maestros.maestros import Maestro
from grupo.grupo import Grupo
from carrera.carrera import Carrera
from datetime import datetime

class Menu:
    escuela = Escuela()
    usuario_estudiante: str = "juan123"
    contrasenia_estudiante: str = "1234"

    usuario_maestro: str= "hilary123"
    contrasenia_maestro: str = "5432"

    def login(self):
        intentos = 0
        while intentos<1 : 
            print("Bienvenido")
            print("Inicie sesion")

            nombre_usuario= input("ingresa usuario")
            contrasenia_usuario = input("ingresa contra")

            if nombre_usuario == self.usuario_estudiante:
                if contrasenia_usuario == self.usuario_estudiante:
                    self.menu_estudiante()
                else:
                    intentos=self.mostrar_intento_sesion_fallido(inrentos_usuario= intentos)

            elif nombre_usuario == self.usuario_maestro:
                if contrasenia_usuario == self.usuario_estudiante:
                    self.menu_maestro()
                else:
                    intentos=self.mostrar_intento_sesion_fallido(inrentos_usuario= intentos)

            else:
                intentos=self.mostrar_intento_sesion_fallido(inrentos_usuario= intentos)
                
        print("max intentos alcanzados bye")

    def menu_estudiante(self):
        print("MENU ESTUDIANTE")

    def menu_maestro(self):
        print("MENU MAESTRO")
            
    def mostrar_intento_sesion_fallido(slef):
            print("usuario o contra mal srry")
            intentos += 1


    def mostrar_menu(self):
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
            print("13. Registrar Carrera")
            print("14. Registrar Semestre")
            print("15. Mostrar Semestre")
            print("16. Mostrar Carrera")
            print("17. Salir")


            opcion = input("Ingresa una opcion para continuar: ")

            if opcion == "1":
                print("Seleccionaste la opcion de registrar")
                
                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa el curp del estudiante: ")
                ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
                contrasenia=input("Ingresa contraseña del estudiante: ")
                fecha_nacimiento = datetime(ano, mes, dia)
                numero_control = self.escuela.generar_numero_control()
                
                estudiante = Estudiante(nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, numero_control=numero_control, contrasenia=contrasenia)
                self.escuela.registrar_estudiante(estudiante)
                print(numero_control)
                print(f"estudiante registrado correctamente {nombre}")


            elif opcion == "2":
                print("Seleccionaste la opcion registrar maestro")
                nombre = input("Ingresa nombre del maestro")
                apellido = input("Ingresa apellido del maestro")
                rfc = input("Ingresa rfc del maestro")
                sueldo = int(input("Ingresa sueldo del maestro"))
                contrasenia=input("Ingresa contraseña del maestro: ")

                numero_control = self.escuela.generar_numero_control(nombre,rfc)
                print(numero_control)
                
                maestro = Maestro(nombre, apellido, rfc, sueldo, contrasenia)
                self.escuela.registrar_maestro(maestro)

            elif opcion == "3":
                nombrem = input("Ingresa rnombre de la materia")
                semestre = int(input("Ingresa no. semestre que la cursa"))
                instructor = input("Ingresa instructor de la materia")
                creditos = int(input("Ingresa no. creditos de la materia"))
                descripcion = input("Ingresa descripcion de la materia")
                id = self.escuela.generar_id_materia(nombrem, semestre, creditos)
                print(id)
                
                materia = Materia(nombrem, instructor, descripcion, semestre, creditos)
                self.escuela.registrar_materia(materia)


            elif opcion == "4":
                tipo = input("Ingresa tipo de grupo A/B")
                id_semestre = input("ID semestre")
                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
                self.escuela.registrar_grupo(grupo=grupo)


            elif opcion == "5":
                pass

            elif opcion == "6":
                self.escuela.listar_estudiantes()
                
            elif opcion == "7":
                self.escuela.listar_maestros()

            elif opcion == "8":
                self.escuela.listar_materia()

            elif opcion == "9":
                self.escuela.listar_grupo()

            elif opcion == "10":
                print("eleccionaste la opcion eliminar estudiante")
                numero_control = input("ingresa el no. control")
                self.escuela.eliminar_estudiante(numero_control=numero_control)

            elif opcion == "11":
                print("eleccionaste la opcion eliminar maestro")
                numero_control = input("ingresa el no. control")
                self.escuela.eliminar_maestro(numero_control=numero_control)

            elif opcion == "12":
                print("eleccionaste la opcion eliminar materia")
                id = input("ingresa el id")
                self.escuela.eliminar_materia(id=id)

            elif opcion == "13":
                nombre = input("Ingresa nombre de la carrera")
                carrera = Carrera(nombre=nombre)

            elif opcion == "14":
                numero = input("Ingresa nombre del semestre")
                id_carrera = input("Ingresa ID  carrera")

                semestre = Semestre(numero=numero, id_carrera=id_carrera)
                self.escuela.registrar_semestre(semestre=semestre)

            elif opcion == "15":
                self.escuela.listar_semestre()

            elif opcion == "16":
                self.escuela.listar_carrera()

            elif opcion == "17":
                print("Hasta luego")
                break
