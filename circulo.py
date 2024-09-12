class Circulo:
    radio = 0

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = (self.radio * self.radio * 3.1416)
        print("Área =", area)

    def calcular_perimetro(self):
        perimetro = (self.radio * 2 * 3.1416)
        print("Perimetro =", perimetro)