import random
print(18*"+")
print("DESCUBRA O NÚMERO")
print(18*"+")
numero_secreto = random.randint(10,100)
print(numero_secreto)
pontos = 100
nivel = int(input("Escolha entre as dificuldades \nFácil (digite 1) \nMédio (digite 2) \nDifícil (digite 3): "))



if nivel == 1:
    jogadas = 30
    perda_serro = 10
    print("Você terá {} jogadas".format(jogadas))
elif nivel == 2:
    jogadas = 10
    perda_serro = 20
    print("Você terá {} jogadas".format(jogadas))
elif nivel == 3:
    jogadas = 5
    perda_serro = 50
    print("Você terá {} jogadas".format(jogadas))
else:
    print("Escolha corretamente sua dificuldade de jogo")



for jogada in range(1, jogadas+1):
    print(f"Tentativa {jogada} de {jogadas}")
    palpite = int(input("Tente descobrir qual o número secreto que está entre 10 e 100: "))
    if 10 <= palpite <= 100:
        if palpite == numero_secreto:
            print("Parabéns você acertou o número secreto {}, você terminou com {} pontos".format(palpite, pontos))
            break
        else:
            if palpite > numero_secreto:
                pontos = pontos - perda_serro
                print("O Número Secreto é MENOR que {}. Você está com {} pontos".format(palpite, pontos))
            elif palpite < numero_secreto:
                pontos = pontos - perda_serro
                print("O Número Secreto é MAIOR que {}. Você está com {} pontos".format(palpite, pontos))
    else:
        print("Digite um palpite válido (entre 10 e 100)")
        
print("FIM")
