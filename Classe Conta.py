class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")


# Testando a conta
conta = Conta(100)

conta.depositar(50)

print(f"Saldo atual: R${conta.get_saldo()}")