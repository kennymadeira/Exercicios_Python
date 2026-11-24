class Produtos:
    def __init__(self, nome, preço, estoque, categoria):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque
        self.categoria = categoria
    
    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: {self.preço}:.2f")
        print(f"Estoque: {self.estoque}")


    def valor_total(self):
        return self.preço * self.estoque
    def aplica_desconto(self):
        self.preço *= (1-10 / 100)
        print(f"Desconto aplicado! Novo preço: R$ {self.preço}")


    def vender(self, quantidade):
        if quantidade > self.estoque:
            print("Estoque insuficiente!")
        else:
            self.estoque -= quantidade
            print(f"Vendido {quantidade} x {self.nome}.Estoque restante: {self.estoque}")


    def repor_estoque(self, quantidade):
        self.estoque += quantidade
        print(f"Novo estoque: {self.estoque}")
def agradecer():
    print("Obrigado pela preferencia, volte sempre!")


prod1 = Produtos("Toddynho", 1.99, 40, "Alimento")
prod2 = Produtos("Batata Frita Congelada", 25.00, 30, "Alimento Congelado")
prod3 = Produtos("Coca-Cola", 14.00, 50, "Bebidas")


while True:
    print("1 - Toddynho")
    print("2 - Batata Frita Congelada")
    print("3 - Coca-Cola")
    print("4 - Finalizar compras")
    print("-" * 40)


    opcao = input("O que deseja comprar?: ")


    if opcao == "1":
        quantidade = int(input("Quantidade: "))
        prod1.vender(quantidade)
        desconto = input("Deseja aplicar desconto (s/n)?: ")
        if desconto == "s":
            prod1.aplica_desconto()
        continue_input = input("Deseja comprar mais alguma coisa? (s/n)?: ")
        if continue_input == "s":
            continue
        else:
            agradecer()
            break
    if opcao == "2":
            quantidade = int(input("Quantidade: "))
            prod2.vender(quantidade)
            desconto = input("Deseja aplicar desconto (s/n)?: ")
            if desconto == "s":
                prod2.aplica_desconto()
            continue_input = input("Deseja comprar mais alguma coisa? (s/n)?: ")
            if continue_input == "s":
                continue
            else:
                agradecer()
                break
    if opcao == "3":
            quantidade = int(input("Quantidade: "))
            prod3.vender(quantidade)
            desconto = input("Deseja aplicar desconto (s/n)?: ")
            if desconto == "s":
                prod3.aplica_desconto()
            continue_input = input("Deseja comprar mais alguma coisa? (s/n)?: ")
            if continue_input == "s":
                continue
            else:
                agradecer()
                break
    elif opcao == "4":
        agradecer()
        break