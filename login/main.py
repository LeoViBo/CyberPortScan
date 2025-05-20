from getpass import getpass
from hashlib import sha256
from json import loads, dumps
from sys import argv

# Codigo para criptografar em hash as senhas

# Não mostra a senha quando esta digitando
# senha = getpass(prompt='OI LINDO< VEM SEMPRE AQUI?')

def cadastrar():
    login = input('Digite o nome desejado\n> ')
    print("")
    senha = hashme(getpass(prompt='Digite sua melhor senha\n> '))
    print("")
    users = get_json()
    if login in users:
        print('Este usuário já existe')
        return
    users[login] = senha
    set_json(users)

def logar():
    login = input('Digite seu login\n> ')
    print("")
    senha = hashme(getpass(prompt='Digite sua senha\n> '))
    print("")
    users = get_json()
    if login not in users: 
        print('==== Usuário ou senha incorretos! ====')
        return
    if users[login] != senha:
        print('==== Usuário ou senha incorretos! ====')
        return
    print('---- Login feito ----')

def hashme(password): return sha256(password.encode()).hexdigest()

def get_json():
    with open('data/contas.json') as f:
        file = f.read()
    return loads(file)

def set_json(json):
    with open('data/contas.json', 'w') as f:
        f.write(dumps(json))

if len(argv) != 2: print("==== error ===="); exit()
if argv[1] == 'cadastrar': cadastrar()
if argv[1] == 'entrar': logar()