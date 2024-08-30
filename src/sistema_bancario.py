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

    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print(f"\n[!] Valor informado: {valor:.2f} "
                  "\nPara depósitos, informe um valor positivo.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if numero_saques >= LIMITE_SAQUES:
            print(f"\n[!] Limite de {LIMITE_SAQUES} saques atingido.")
        elif valor > saldo:
            print(f"\n[!] Saldo insuficiente. R$ {saldo:.2f}")
        elif valor > limite:
            print(f"\n[!] O montante solicitado para saque ultrapassa o limite permitido de R$ {limite:.2f}")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque...: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print(f"\n[!] Valor informado: {valor:.2f} "
                  "\nPara saques, informe um valor positivo.")

    elif opcao == "e":
        extrato_titulo = " Extrato "
        print(extrato_titulo.center(35, '#'))
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"Saldo...: R$ {saldo:.2f}")
        print("#" * 35)

    elif opcao == "q":
        break

    else:
        print("\n[!] A opção selecionada não existe. \nPor favor, escolha uma das opções abaixo:")
