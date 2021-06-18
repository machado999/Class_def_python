#defindo os calculos
class cal:
    def __init__(self, num1 , num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b
    def mutilicacao(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b
    def subtracao(self):
        return self.valor_a - self.valor_b
#interação com o úsuario
num1 = int(input('digite 1° número: '))
num2 = int(input('digite 2° número: '))
#definindo os valores dos calculos de acordo com os input
bilobs = cal(num1 , num2)
#imprimindo os valores na tela
if __name__ == '__main__':
    print("Valor de soma,",num1,'+',num2,'=' ,cal.soma(bilobs))
    print('Valor de multiplicação:',num1,'*',num2,'=',cal.mutilicacao(bilobs))
    print('Valor de divisão:',num1,'/',num2,'=',cal.divisao(bilobs))
    print('Valor de subtração:',num1,'-',num2,'=',cal.subtracao(bilobs))
