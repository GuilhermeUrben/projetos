# Bem vindos ao imprensadinho
# O objetivo é imprensar o computador.
# O computador irá gerar um valor aleatório, onde o usuário terá que chutar valores próximos até imprensar o computador.
# Exemplo: Computador gerou um valor aleatório = 64, o usuário terá que chutar valores até encontrar os números 63, e 65 sem falar o valor 64.
# Exemplo: Valor aleatório = 64
# Menor valor digitado pelo usuário = 63
# Maior valor digitado pelo usuário = 65
# Caso o usuário fale o valor igual o valor gerado pelo computador, ele perde.

import random


# criando variáveis
class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.menor_chute = self.valor_minimo
        self.maior_chute = self.valor_maximo
        self.tentar_novamente = True

# Criando função para pedir os valores (chutes) do usuário.
    def PedirValorAleatorio(self):
        if self.menor_chute == self.maior_chute:
            print(
                f"Você já fez uma tentativa, mas o número não está nesse intervalo. Tente novamente.")
        else:
            self.valor_do_chute = int(
                input(f'Chute um número entre {self.menor_chute} e {self.maior_chute}: '))
            if (self.valor_do_chute == self.valor_aleatorio + 1 or self.valor_do_chute == self.valor_aleatorio - 1) and self.valor_do_chute == self.menor_chute + 1:
                print(
                    f'PARABÉNS!! Você venceu imprensando o computador. O número aleatório era {self.valor_aleatorio}.')
                self.tentar_novamente = False
            elif self.valor_do_chute < self.valor_aleatorio:
                print("Seu chute está muito baixo.")
                self.menor_chute = max(self.menor_chute, self.valor_do_chute)
            elif self.valor_do_chute > self.valor_aleatorio:
                print("Seu chute está muito alto.")
                self.maior_chute = min(self.maior_chute, self.valor_do_chute)
            elif self.valor_do_chute == self.valor_aleatorio:
                print("Você acertou o número em cheio, portanto, você perdeu!")
                self.tentar_novamente = False

# Função para gerar o valor aleátorio pelo computador.
    def GerarNumeroAleatorio(self):
        return random.randint(self.valor_minimo, self.valor_maximo)

# Função para pedir um valor inicial, tendo uma base para o usuário continuar os chutes.
    def Iniciar(self):
        self.valor_aleatorio = self.GerarNumeroAleatorio()
        while self.tentar_novamente and self.menor_chute <= self.maior_chute:
            self.PedirValorAleatorio()
        if self.menor_chute > self.maior_chute:
            print(
                f'Você não acertou o número. O número aleatório era {self.valor_aleatorio}.')


chute = ChuteONumero()
chute.Iniciar()
