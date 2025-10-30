try:
    saldo = float(input("Digite o saldo da sua conta: R$ "))
    transferencia = float(input("Digite o valor da transferência: R$ "))

    if transferencia > saldo:
        raise ValueError("Saldo insuficiente.")

    saldo -= transferencia
    print(f"Transferência realizada com sucesso! Saldo atual: R$ {saldo:.2f}")

except ValueError as e:
    print("Erro:", e)
