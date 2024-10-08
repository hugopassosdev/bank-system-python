menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito <= 0:
            print("Valor inválido, por favor digite um valor maior que 0!")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito}\n"
            print("Depósito efetuado com sucesso!")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= 0:
            print("Valor inválido, por favor digite um valor maior que 0!")
        elif valor_saque > saldo + limite:
            print("Saldo insuficiente!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido!")
        else:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso!")
    elif opcao == "e":
        print(f"Saldo: R$ {saldo}")
        print(f"Limite: R$ {limite}")
    elif opcao == "q":
        break
    else:
        print("Opção inválida, por favor selecioine uma opção válida!")