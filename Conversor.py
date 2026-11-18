def converter_temperatura(C):
    F = (C * 1.8) + 32
    return F


def converter_km(Km):
    Milhas = Km * 0.621371
    return Milhas


def converter_kg(Kg):
    Libras = Kg * 2.20462
    return Libras


while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1. Celsius para Fahrenheit")
    print("2. Km para Milhas")
    print("3. Kg para Libras")
    print("4. Sair")

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
        print("\nPrograma encerrado. Até mais!")
        break

    else:
        print("\nOpção inválida! Escolha uma opção de 1 a 4.")