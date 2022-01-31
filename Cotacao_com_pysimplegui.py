import PySimpleGUI as sg
import requests

class Cotacao:
    def __init__(self):
        sg.theme('SystemDefault')
        layout = [
            [sg.Text('Bem vindo ao app de cotação de moedas')],
            [sg.Text('Essas são as moedas mais cotadas')],
            [sg.Text('USD:'), sg.Text(self.pegar_cotacao('usd'))],
            [sg.Text('EUR:'), sg.Text(self.pegar_cotacao('eur'))],
            [sg.Text('BTC:'), sg.Text(self.pegar_cotacao('btc'))],
            [sg.Text('ETH:'), sg.Text(self.pegar_cotacao('eth'))],
            [sg.Text('Qual moeda vai quer cotar agora?')],
            [sg.Input(key='moeda')],
            [sg.Button('Cotar')],
            [sg.Output(size=(50, 7))]
        ]
        self.janela = sg.Window('Cotações', layout)

    def pegar_cotacao(self,moeda):
        moeda = moeda.upper()
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = float(requests.get(link).json()[f'{moeda}BRL']['bid'])
        requisicao = "${:,.2f}".format(requisicao)
        print(f' Cotacao da moeda {moeda}: {requisicao}')
        return requisicao

    def iniciar(self):
        while True:
            event, valores = self.janela.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Cotar':
                self.pegar_cotacao(valores['moeda'])


cot = Cotacao()
cot.iniciar()




