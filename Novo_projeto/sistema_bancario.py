def deposito(saldo: float, valor: float) -> float:
    if valor <= 0:
        print("Valor inválido para depósito.")
        return 0.0

    return saldo + valor

def saque(saldo: float, valor: float) -> float:
    if valor <= 0:
        print("Valor inválido para saque.")
        return 0.0

    if valor > saldo:
        print("Saldo insuficiente para saque.")
        return saldo

    return saldo - valor

def mostrar_saldo(saldo: float) -> None:
    print(f"Saldo atual: R$ {saldo:.2f}")


    