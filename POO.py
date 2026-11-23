class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque

p1 = Produto("Arroz", 5.99, 30)
p2 = Produto("Macarrão", 8.5, 80)

print(type(p1))
print(p1)
print(p1 == p2)

print(p1.nome)
print(p1.preço)
print(p1.estoque)