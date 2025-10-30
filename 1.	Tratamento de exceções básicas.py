try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 / num2

except ValueError:
    print("Erro: Você deve digitar apenas números.")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

else:
    print(f"O resultado da divisão é: {resultado:.2f}")
