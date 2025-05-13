titular = str(input("Titular da Conta: "))

conta = [0]
historico = []

controle = True

while controle == True:
    menu = int(input("Oque deseja? \n 1- Depositar \n 2- Sacar \n 3- Consultar Saldo \n 4- Consultar Histórico \n 5- Sair\n "))
    if menu == 1:
        deposito = float(input("Depósito: "))
        if deposito <= 0:
            deposito = 0
            print("Digite um valor válido para depósito.")
        else:
            conta[0] += deposito
            print("Você depositou R$ {} na sua conta".format(deposito))
            historico.append(deposito)
    elif menu == 2:
        saque = float(input("Deseja sacar quanto? "))
        if saque <= 0:
            print("Digite um valor válido para saque.")
        elif conta[0] == 0:
            print("Você não possui saldo. Deposite primeiro para poder sacar.")
        elif saque > conta[0]:
            print("Seu saldo é insuficiente para esse valor de Saque, verifique seu saldo.")
        else:
            conta[0] = conta[0] - saque
            print("Você sacou R$ {} da sua conta.".format(saque))
            historico.append(-saque)
    elif menu == 3:
        print("Saldo da Conta: R$ {}".format(conta))
    elif menu == 4:
        print("Esse é o histórico da conta: {}".format(historico))
    else:
        controle == False
        print("Obrigado pela preferência Sr(a). {}".format(titular))
        break