import toolbox
import urllib.request

toolbox.cabecalho(' Site está acessível? ')
toolbox.paragrafo(' Tentando contatar o pudim... ')

try:
    conexao = urllib.request.urlopen('https://pudim.com.br/', timeout=5)
except urllib.error.URLError:
    print('\33[31mNão consegui acessar o PUDIM!')
else:
    print('\33[32mConsegui contatar o Pudim!')

toolbox.fimLinha()