# Constantes
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500

# Variáveis
usuarios = []
contas = []
numero_conta = 1

# Classes
class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, agencia, numero, usuario):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

# Funções
def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Erro: CPF já cadastrado.")
            return
    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")

def cadastrar_conta(usuario):
    global numero_conta
    nova_conta = ContaBancaria("0001", numero_conta, usuario)
    contas.append(nova_conta)
    numero_conta += 1
    print("Conta cadastrada com sucesso.")

def listar_contas():
    print("\n========== LISTA DE CONTAS ==========")
    for conta in contas:
        print(f"Agência: {conta.agencia} | Número da Conta: {conta.numero} | Nome do Cliente: {conta.usuario.nome}")
    print("======================================")

def sacar(nome, valor):
    for conta in contas:
        if conta.usuario.nome == nome:
            excedeu_saldo = valor > conta.saldo
            excedeu_limite = valor > LIMITE_SAQUE_VALOR
            excedeu_saques = conta.numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                conta.saldo -= valor
                conta.extrato += f"Saque: R$ {valor:.2f}\n"
                conta.numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")
            return
    print("Usuário não encontrado.")

def depositar(valor, nome):
    for conta in contas:
        if conta.usuario.nome == nome:
            if valor > 0:
                conta.saldo += valor
                conta.extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")
            return
    print("Usuário não encontrado.")

def extrato(nome, saldo_atual, extrato_atual):
    for conta in contas:
        if conta.usuario.nome == nome:
            print("\n========== EXTRATO ==========")
            print(conta.extrato)
            print(f"Saldo: R$ {conta.saldo:.2f}")
            print("=============================")
            return
    print("Usuário não encontrado.")

# Menu
menu = """
[u] Cadastrar Usuário
[c] Cadastrar Conta
[l] Listar Contas
[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        cadastrar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("CPF do Usuário: ")
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.cpf == cpf:
                usuario_encontrado = usuario
                break
        if usuario_encontrado:
            cadastrar_conta(usuario_encontrado)
        else:
            print("Usuário não encontrado.")

    elif opcao == "l":
        listar_contas()

    elif opcao == "s":
        nome = input("Nome do Cliente: ")
        valor = float(input("Valor do Saque: "))
        sacar(nome, valor)

    elif opcao == "d":
        nome = input("Nome do Cliente: ")
        valor = float(input("Valor do Depósito: "))
        depositar(valor, nome)

    elif opcao == "e":
        nome = input("Nome do Cliente: ")
        extrato(nome, saldo_atual=None, extrato_atual=None)

    elif opcao == "q":
        break
