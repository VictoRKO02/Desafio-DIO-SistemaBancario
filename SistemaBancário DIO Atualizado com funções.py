import textwrap
from datetime import datetime

def opcoes():
    opcoes = """Olá, seja bem-vindo ao Banco da DIO! Por favor, escolha uma das opções abaixo:
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [4] - Criar conta 
    [5] - Listar contas
    [6] - Novo usuário
    [7] - Sair
    """
    try:
        escolha = int(input(textwrap.dedent(opcoes)))
        if escolha not in range(1, 8):
            print("Opção inválida. Por favor, escolha um número entre 1 e 7.")
            return 0
        return escolha
    except ValueError:
        print("Entrada inválida. Por favor, insira um número entre 1 e 7.")
        return 0

def depositar(saldo, valor_deposito, extrato):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito:\t+R$ {valor_deposito:.2f} (Saldo: R$ {saldo:.2f})\n"
        print(f"Você depositou R$ {valor_deposito:.2f}. Saldo atual: R$ {saldo:.2f}")
    else: 
        print("O valor digitado deve ser maior que zero.")
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, saques_diarios, limite_saques):
    ultrapassou_saldo = valor_saque > saldo
    ultrapassou_limite = valor_saque > limite
    ultrapassou_saques = saques_diarios >= limite_saques

    if ultrapassou_saldo:
        print("Não será possível sacar o dinheiro por falta de saldo. Por favor, escolha outro valor.")
    elif ultrapassou_limite:
        print("Não será possível sacar o valor desejado. O limite por saque é de R$ 500,00.")
    elif ultrapassou_saques:
        print("Você atingiu o limite de saques diários.")
    elif valor_saque > 0:
        saldo -= valor_saque
        saques_diarios += 1
        extrato += f"Saque:\t\t-R$ {valor_saque:.2f} (Saldo: R$ {saldo:.2f})\n"
        print(f"Você sacou R$ {valor_saque:.2f}. Saldo atual: R$ {saldo:.2f}")
    else: 
        print("O valor informado é inválido.")
    return saldo, extrato, saques_diarios

def exibir_extrato(saldo, *, extrato):
    print("Exibindo extrato...")
    if extrato:
        print(extrato)
    else:
        print("Nenhuma operação realizada.")
    print(f"Saldo atual: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtro(cpf, usuarios)

    if usuario:
        print("Este CPF já existe em nossa base de dados!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtro(cpf, usuarios):
    filtro_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro_usuario[0] if filtro_usuario else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    if contas:
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))
    else:
        print("Nenhuma conta encontrada.")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    LIMITE_DEPOSITO_SAQUE = 500

    extrato = ""
    saldo = 0
    saques_diarios = 0
    usuarios = []
    contas = []

    while True:
        escolha = opcoes()

        if escolha == 1:
            try:
                valor_deposito = float(input("Digite o valor a ser depositado: "))
                saldo, extrato = depositar(saldo, valor_deposito, extrato)
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico.")

        elif escolha == 2:
            try:
                valor_saque = float(input("Digite o valor a ser sacado: "))
                saldo, extrato, saques_diarios = sacar(
                    saldo=saldo,
                    valor_saque=valor_saque,
                    extrato=extrato,
                    limite=LIMITE_DEPOSITO_SAQUE,
                    saques_diarios=saques_diarios,
                    limite_saques=LIMITE_SAQUES,
                )
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico.")
        
        elif escolha == 3:
            exibir_extrato(saldo, extrato=extrato)
        
        elif escolha == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                extrato += f"Conta criada:\tAgência: {conta['agencia']}, C/C: {conta['numero_conta']}\n"
        
        elif escolha == 5:
            listar_contas(contas)
        
        elif escolha == 6:
            criar_usuario(usuarios)
        
        elif escolha == 7:
            print("Saindo do sistema. Obrigado por usar o Banco da DIO!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
