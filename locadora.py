import os

carros = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130),
]

alugados = []

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("===============")
    print("Bem-vindo à locadora de carros")
    print("===============")
    print("0 - Mostrar carros")
    print("1 - Alugar carro")
    print("2 - Devolver carro")
    print("3 - Sair")
    print("===============")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        for i, carro in enumerate(carros):
            print(f"[{i}] {carro[0]} - R$ {carro[1]}/dia")
        input("\nPressione ENTER para voltar ao menu.")

    elif opcao == "1":
        if len(carros) == 0:
            print("Não há carros disponíveis.")
            input("\nPressione ENTER para voltar ao menu.")
            continue

        for i, carro in enumerate(carros):
            print(f"[{i}] {carro[0]} - R$ {carro[1]}/dia")

        cod = int(input("Digite o código do carro: "))
        dias = int(input("Por quantos dias deseja alugar? "))
        total = carros[cod][1] * dias

        print(f"\nVocê escolheu: {carros[cod][0]} por {dias} dias")
        print(f"Total a pagar: R$ {total}")

        confirma = input("Confirmar aluguel? (s/n): ").lower()
        if confirma == "s":
            alugados.append(carros.pop(cod))
            print("Carro alugado com sucesso!")

        input("\nPressione ENTER para voltar ao menu.")

    elif opcao == "2":
        if len(alugados) == 0:
            print("Você não tem carros alugados.")
            input("\nPressione ENTER para voltar ao menu.")
            continue

        for i, carro in enumerate(alugados):
            print(f"[{i}] {carro[0]} - R$ {carro[1]}/dia")

        cod = int(input("Digite o código do carro para devolver: "))
        carros.append(alugados.pop(cod))
        print("Carro devolvido com sucesso!")

        input("\nPressione ENTER para voltar ao menu.")

    elif opcao == "3":
        print("Obrigado por utilizar nossa locadora!")
        break

    else:
        print("Opção inválida.")
        input("\nPressione ENTER para voltar ao menu.")
