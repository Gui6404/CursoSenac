def soma(a,b):
    s = a + b
    print("{} + {} = {}".format(a,b,s))

def subtrai(a,b):
    st = a - b
    print("{} - {} = {}".format(a,b,st))

def multi(a,b):
    m = a*b
    print("{} X {} = {}".format(a,b,m))

def div(a,b):
    d = a/b
    print("{} / {} = {}".format(a,b,d))

def calculadora(a,b):
    menu = int(input(" 1- Somar \n 2- Subtrair \n 3- Multiplicar \n 4- Dividir \n Qual operação deseja? "))
    if menu == 1:
        soma(a,b)
    elif menu == 2:
        subtrai(a,b)
    elif menu == 3:
        multi(a,b)
    else:
        div(a,b)

c = int(input("Digite um número: "))
d = int(input("Digite outro número: "))
        
calculadora(c,d)
