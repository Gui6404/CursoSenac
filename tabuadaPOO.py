class Tabuada:
    def __init__(self,num):
        self.num = num
        self._resultado = 0 
    
    def soma(self):
        if self.num != 0:
            for i in range(1,11):
                self._resultado = self.num + i
                print(f"{self.num} + {i} = {self._resultado}")
        else:
            print("Digite um valor diferente de 0")

    def subtrai(self):
        if self.num != 0:
            for i in range(1,11):
                self._resultado = self.num - i
                print(f"{self.num} - {i} = {self._resultado}")
        else:
            print("Digite um valor diferente de 0")

    def multi(self):
        if self.num != 0:
            for i in range(1,11):
                self._resultado = self.num * i
                print(f"{self.num} x {i} = {self._resultado}")
        else:
            print("Digite um valor diferente de 0")

    def div(self):
        if self.num != 0:
            for i in range(1,11):
                self._resultado = self.num / i
                print(f"{self.num} / {i} = {self._resultado}")
        else:
            print("Digite um valor diferente de 0")


teste = Tabuada(2)

teste.soma()
teste.subtrai()
teste.multi()
teste.div()

