try:
    numero = float(input("Digite um número: "))
    if numero > 10:
        print("Número válido!")
    else:
        print("Número inválido! Deve ser maior que 10.")
except ValueError:
    print("Erro: Digite apenas números válidos.")
else:
    print("Programa executado com sucesso!")
finally:
    print("Programa encerrado.")
