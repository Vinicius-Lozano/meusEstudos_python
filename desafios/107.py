import moeda107
import toolbox

toolbox.cabecalho(' Exercitando módulos em Python ')

num = float(input('\33[34mDigite o preço desejado:\33[33m '))
print(f'\33[34mA metade de \33[33m {num:.0f} \33[34m é \33[33m {moeda107.metade(num):.1f}')
print(f'\33[34mO dobro de \33[33m {num:.0f} \33[34m é \33[33m {moeda107.dobro(num):.1f}')
print(f'\33[34mO aumento de 10% de \33[33m {num:.0f} \33[34m é \33[33m {moeda107.aumentar(num, 10):.1f}')
print(f'\33[34mO desconto de 10% de \33[33m {num:.0f} \33[34m é \33[33m {moeda107.diminuir(num, 10):.1f}')
toolbox.fimLinha()