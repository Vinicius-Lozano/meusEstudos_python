from moeda111 import moeda
import toolbox

toolbox.cabecalho(' Exercitando módulos em Python ')

num = float(input('\33[34mDigite o preço desejado: \33[33mR$'))
moeda.resumo(num, 25, 20)
toolbox.fimLinha()