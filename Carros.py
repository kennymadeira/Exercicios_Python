class Carros:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("-" * 80)


p1 = Carros("Declasse", "Tulip", "1972")
p2 = Carros("Declasse", "Sabre Turbo", "1970")

p1.exibir()
p2.exibir()
