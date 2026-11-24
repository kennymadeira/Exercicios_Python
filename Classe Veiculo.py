class Veiculo:
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max


    def mover(self):
        print(f"O veículo {self.marca} está se movendo.")


class Carro(Veiculo):
    def __init__(self, marca, velocidade_max, num_portas):
        super().__init__(marca, velocidade_max)
        self.num_portas = num_portas


    def mover(self):
        print(f"O carro {self.marca} está andando a até {self.velocidade_max} km/h.")


class Bicicleta(Veiculo):
    def __init__(self, marca, velocidade_max, num_marchas):
        super().__init__(marca, velocidade_max)
        self.num_marchas = num_marchas


    def mover(self):
        print(f"A bicicleta {self.marca} está pedalando com {self.num_marchas} marchas.")


# Criando os objetos
carro1 = Carro("Toyota", 200, 4)
bicicleta1 = Bicicleta("Caloi", 40, 21)




# Exibindo informações
carro1.mover()
bicicleta1.mover()