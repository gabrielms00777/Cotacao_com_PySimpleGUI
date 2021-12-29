import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window
import requests

sg.theme('Dark')

def Pegar_cotacao(moeda):
    link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    cotacao = dic_requisicao[f'{moeda}BRL']['bid']
    return cotacao

layout = [
    [sg.Text(f'Dolar: {Pegar_cotacao("USD")}',key='dolar')],
    [sg.Text(f'Euro: {Pegar_cotacao("EUR")}',key='euro')],
    [sg.Text(f'Bitcoin: {Pegar_cotacao("BTC")}',key='btc')],
    [sg.Text(f'Etherum: {Pegar_cotacao("ETH")}',key='eth')]
]

window = sg.Window('Cotação Medas', layout)

window.read()


