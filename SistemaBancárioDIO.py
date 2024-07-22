opcoes = """Olá, seja bem-vindo ao Banco da DIO! Por favor, escolha uma das opções abaixo:
[1] - Saque
[2] - Depósito
[3] - Extrato
"""

extrato = ""
saldo = 0
saques_diarios = 0
limite_saques_diarios = 3
limite_saque = 500

continuar = 's'

while continuar.lower() == 's':
    print(opcoes)

    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
        if saques_diarios >= limite_saques_diarios:
            print("Você atingiu o limite de saques diários.")
        else:
            valor_saque = float(input("Digite o valor desejado a ser sacado: "))
            if valor_saque > saldo:
                print("Não será possível sacar o dinheiro por falta de saldo. Por favor, escolha outro valor.")
            elif valor_saque > limite_saque:
                print("Não será possível sacar o valor desejado. O limite por saque é de R$ 500,00.")
            elif valor_saque <= 0:
                print("O valor digitado deve ser maior que zero.")
            else:
                saldo -= valor_saque
                saques_diarios += 1
                extrato += f"Saque: -R${valor_saque:.2f} (Saldo: R${saldo:.2f})\n"
                print(f"Você sacou R${valor_saque:.2f}. Saldo atual: R${saldo:.2f}")

    elif escolha == 2:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito <= 0:
            print("O valor digitado deve ser maior que zero.")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: +R${valor_deposito:.2f} (Saldo: R${saldo:.2f})\n"
            print(f"Você depositou R${valor_deposito:.2f}. Saldo atual: R${saldo:.2f}")

    elif escolha == 3:
        print("Exibindo extrato...")
        if extrato:
            print(extrato)
        else:
            print("Nenhuma operação realizada.")

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")

    continuar = input("Deseja realizar outra operação? (s/n): ")

print("Obrigado por usar o Banco da DIO!")
