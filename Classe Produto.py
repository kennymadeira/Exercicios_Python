class Produtos:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque


    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preço:.2f}")
        print(f"Estoque: {self.estoque}")
        print("-" * 40)


    def vender(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida!")


        elif quantidade <= self.estoque:
            self.estoque -= quantidade
            total = quantidade * self.preço


            print("Venda realizada com sucesso!")
            print(f"Total da compra: R$ {total:.2f}")


        else:
            print("Estoque insuficiente!")




# Criando os produtos
prod1 = Produtos("Banana", 4.50, 20)
prod2 = Produtos("Morango", 11.00, 30)
prod3 = Produtos("Acerola", 2.00, 50)


# Menu de compras
while True:
    print("\n===== MERCADO =====")
    print("1 - Banana")
    print("2 - Morango")
    print("3 - Acerola")
    print("4 - Ver estoque")
    print("5 - Sair")


    opcao = input("O que deseja comprar? ")


    if opcao == "1":
        quantidade = int(input("Quantidade: "))
        prod1.vender(quantidade)


    elif opcao == "2":
        quantidade = int(input("Quantidade: "))
        prod2.vender(quantidade)


    elif opcao == "3":
        quantidade = int(input("Quantidade: "))
        prod3.vender(quantidade)


    elif opcao == "4":
        prod1.exibir()
        prod2.exibir()
        prod3.exibir()


    elif opcao == "5":
        print("Obrigado pela compra! Volte sempre!")
        break


    else:
        print("Opção inválida!")

