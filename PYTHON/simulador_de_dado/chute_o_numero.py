# chute o número
# Criar um algorítimo que gera um valor aleatório e eu tenho que ficar tentando o número até acertar

import random


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.maior_chute = 0
        self.menor_chute = 1
        self.tentar_novamente = True


    def ValorInicial(self):
        if self.valor_inicial > self.menor_chute and self.valor_inicial < self.maior_chute:
            self.menor_chute = self.valor_inicial
        if self.valor_inicial > self.maior_chute and self.valor_inicial > self.menor_chute:
            self.maior_chute = self.valor_inicial

    def PedirValorAleatorio(self):
        self.ValorInicial()
        self.valor_do_chute = int(input(f'Chute um número entre {self.menor_chute} e {self.maior_chute}: '))
        if self.valor_do_chute > self.menor_chute and self.valor_do_chute < self.maior_chute:
            self.menor_chute = self.valor_do_chute  
        if self.valor_do_chute > self.maior_chute and self.valor_do_chute > self.menor_chute:
            self.maior_chute = self.valor_do_chute

    def GerarNumeroAleatorio(self):
        return random.randint(self.valor_minimo, self.valor_maximo)

    def Iniciar(self):
        self.valor_inicial = int(input('Chute um número entre 1 e 100: '))
        self.valor_aleatorio = self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.valor_do_chute != self.valor_aleatorio:
                self.PedirValorAleatorio()
        else:
            print(
                f'PARABÉNS!! Você acertou, o número aleatório era {self.valor_aleatorio}.')


chute = ChuteONumero()
chute.Iniciar()
