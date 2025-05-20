from request import get

# Codigo de retorno do ip do site (ex de input: https://www.fiap.com.br)
print(get(input('Digite o alvo:\n> ')).status_code)