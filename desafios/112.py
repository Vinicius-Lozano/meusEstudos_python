from moeda111 import moeda, dados
import toolbox

toolbox.cabecalho(' Exercitando módulos em Python ')

num = dados.leiaDinheiro('\33[34mDigite o preço desejado: \33[33mR$')
moeda.resumo(num, 25, 20)
toolbox.fimLinha()