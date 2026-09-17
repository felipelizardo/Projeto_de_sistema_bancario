from sistema_bancario import deposito, saque, mostrar_saldo


def menu():
    print("=== Sistema Bancário ===")
    print("1. Depósito")
    print("2. Saque")
    print("3. Mostrar Saldo")
    print("4. Sair")


def iniciar_banco():
    saldo = 0.0

    while True:
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                valor = float(input("Digite o valor do depósito: "))
                saldo = deposito(saldo, valor)
                print("Depósito realizado.")

            elif opcao == 2:
                valor = float(input("Digite o valor do saque: "))
                saldo = saque(saldo, valor)
                print("Saque realizado.")

            elif opcao == 3:
                mostrar_saldo(saldo)

            elif opcao == 4:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção do menu.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número válido.")


if __name__ == "__main__":
    iniciar_banco()

