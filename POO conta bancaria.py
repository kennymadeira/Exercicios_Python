class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo   # privado

    def get_saldo(self):       # getter  
        return self.__saldo

    def depositas(self, valor): # setter
        if valor > 0:
            self.__saldo += valor