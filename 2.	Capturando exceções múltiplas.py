cores = {'vermelho': (255, 0, 0), 
         'verde': (0, 255, 0), 
         'azul': (0, 0, 255)}

try:
    cor = input("Digite o nome de uma cor (vermelho, verde ou azul): ").lower()
    valor_rgb = cores[cor]
    print("O valor RGB da cor", cor, "é", valor_rgb)
except KeyError:
    print("Erro: Essa cor não existe no dicionário.")
