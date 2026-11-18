def converter_temperatura(C):
    F = (C * 1.8) + 32
    return F


def converter_km(Km):
    Milhas = Km * 0.621371
    return Milhas


def converter_kg(Kg):
    Libras = Kg * 2.20462
    return Libras

def calcular_area_retangulo(largura, comprimento):
    area = largura * comprimento
    return area

def maior_de_tres(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
def listar_primos():
    primos = []
    for numero in range(1, 101):
        if verificar_primo(numero):
            primos.append(numero)
    return primos


while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1. Celsius para Fahrenheit")
    print("2. Km para Milhas")
    print("3. Kg para Libras")
    print("4. Area do Retangulo")
    print("5. Função maior de 3")
    print("6. conferir se o numero é primo")
    print("0. Sair")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        print("\nVamos converter Celsius para Fahrenheit!")

        C = float(input("Digite a temperatura em Celsius: "))
        F = converter_temperatura(C)

        print(f"A temperatura em Fahrenheit é: {F:.2f}°F")

    elif opcao == "2":
        print("\nVamos converter Km para Milhas!")

        Km = float(input("Digite a distância em quilômetros: "))
        Milhas = converter_km(Km)

        print(f"A distância em milhas é: {Milhas:.2f} milhas")

    elif opcao == "3":
        print("\nVamos converter Kg para Libras!")

        Kg = float(input("Digite o peso em quilogramas: "))
        Libras = converter_kg(Kg)

        print(f"O peso em libras é: {Libras:.2f} libras")

    elif opcao == "4":
        print("\nVamos calcular a Area de um Triangulo")
        largura = float(input("Digite a largura do retângulo: "))
        comprimento = float(input("Digite o comprimento do retângulo: "))
        resultado = calcular_area_retangulo(largura, comprimento)

        print(f"A área do retângulo é: {resultado}")

    elif opcao == "5":
        print("\nVamos fazer uma função maior de 3")
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        numero3 = int(input("Digite o terceiro número: "))
        resultado = maior_de_tres(numero1, numero2, numero3)
        print("O maior número é:", resultado)

    elif opcao == "6":
        numero = int(input("Digite um número inteiro: "))
        if verificar_primo(numero):
            print(f"O número {numero} é primo!")
        else:
            print(f"O número {numero} não é primo.")
            print("Lista de números primos de 1 a 100:")
            print(listar_primos())
    

    elif opcao == "0":
        print("\nPrograma encerrado. Até mais!")
        break

    else:
        print("\nOpção inválida! Escolha uma opção de 1 a 4.")