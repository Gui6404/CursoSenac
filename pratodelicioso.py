import random

print(30*"+")
print("DESCUBRA O PRATO DELICIOSO")
print(30*"+")

pratos = ["Feijoada","Lasanha","Churrasco","Moqueca","Estrogonofe","Frango à parmegiana","Bobó de camarão","Tacos","Pizza","Sushi","Yakissoba","Risoto de cogumelos","Hambúrguer artesanal","Ceviche","Cuscuz nordestino","Nhoque ao sugo","Paella","Macarronada","Carne de sol com mandioca","Ratatouille"]

prato_secreto = random.choice(pratos)
print(prato_secreto)
nivel = int(input("Escolha entre as dificuldades \nFácil (digite 1) \nMédio (digite 2) \nDifícil (digite 3): "))

if nivel == 1:
    jogadas = 30
    print("Você terá {} jogadas".format(jogadas))
elif nivel == 2:
    jogadas = 10
    print("Você terá {} jogadas".format(jogadas))
elif nivel == 3:
    jogadas = 5
    print("Você terá {} jogadas".format(jogadas))
else:
    print("Escolha corretamente sua dificuldade de jogo")



for jogada in range(1, jogadas+1): 
    palpite = str(input("Qual o prato delicioso secreto ? "))
    if palpite == prato_secreto:
        print("Parabéns você acertou o prato secreto! {} é delicioso mesmo!".format(palpite))
        break
    else:
        restam = (jogadas) - jogada
        print("Você errou! Restam {} tentativas".format(restam))
