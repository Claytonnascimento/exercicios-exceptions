class SenhaInvalidaError(Exception):
    pass

def verificar_senha(senha):
    if len(senha) < 8:
        raise SenhaInvalidaError("Senha inválida: deve ter no mínimo 8 caracteres.")
    if not any(char.isdigit() for char in senha):
        raise SenhaInvalidaError("Senha inválida: deve conter pelo menos um número.")
    print("Senha válida!")

try:
    senha = input("Digite sua senha: ")
    verificar_senha(senha)
except SenhaInvalidaError as e:
    print(e)
