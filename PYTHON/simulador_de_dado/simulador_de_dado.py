# Simulador de dado
# Simular o uso de um dado gerando um valor de 1 até 6

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Gerar um novo valor para o dado?'
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):
        # criar janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        while True:
            try:
                    if self.eventos == 'sim' or self.eventos == 's':
                        self.GerarValorDoDado()
                        break
                    elif self.eventos =='não' or self.eventos == 'n':
                        print('Agradecemos a sua participação.')
                        break
                    else:
                        print('Favor digitar sim ou não')
                        break
            except:
                    print('Ocorreu um erro ao receber sua resposta.')     
                    
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()