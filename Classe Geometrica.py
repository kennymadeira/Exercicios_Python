import math


class Figura:
    def calcular_area(self):
        pass




class Retangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcular_area(self):
        print(f"A área do retângulo é {self.base * self.altura}")




class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio


    def calcular_area(self):
        print(f"A área do círculo é {math.pi * self.raio ** 2:.2f}")




# Criando os objetos
retangulo1 = Retangulo(10, 5)
circulo1 = Circulo(3)


# Mostrando as áreas
retangulo1.calcular_area()
circulo1.calcular_area()