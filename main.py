from circulo import Circulo 

while True:
    print("\n*** BIENVENIDO ***")
    print("Opciones en el Sistema")
    print("1. Calcular Area")
    print("2. Calcular Perimetro")
    print("3. Salir")

    opcion = input("Ingresa la opción que deseas: ")

    if opcion == "1":
        radio = int(input("\n Escribir Radio del Circulo \n"))
        circulo = Circulo(radio)
        circulo.calcular_area()
    elif opcion == "2":
        radio = int(input("\n Escribir Radio del Circulo \n"))
        circulo = Circulo(radio)
        circulo.calcular_perimetro()
    elif opcion == "3":
        print("\nHasta luego")
        break