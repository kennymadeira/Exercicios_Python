class FUNCIONARIO:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base


    def calcular_salario(self):
        return self.salario_base




class GERENTE(FUNCIONARIO):
    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 0.20)




class ESTAGIARIO(FUNCIONARIO):
    def calcular_salario(self):
        return self.salario_base




# Criando os objetos
gerente = GERENTE("Carlos", 5000)
estagiario = ESTAGIARIO("Ana", 1500)


# Exibindo os resultados
print("Gerente:", gerente.nome)
print("Salário:", gerente.calcular_salario())


print("\nEstagiário:", estagiario.nome)
print("Salário:", estagiario.calcular_salario())