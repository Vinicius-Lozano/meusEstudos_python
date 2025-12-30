import moeda108
import toolbox

toolbox.cabecalho(' Exercitando módulos em Python ')

num = float(input('\33[34mDigite o preço desejado: R$\33[33m'))
print(f'\33[34mA metade de \33[33m R${num:.0f} \33[34m é \33[33m {moeda108.moeda(moeda108.metade(num))}')
print(f'\33[34mO dobro de \33[33m R${num:.0f} \33[34m é \33[33m {moeda108.moeda(moeda108.dobro(num))}')
print(f'\33[34mO aumento de 10% de \33[33m R${num:.0f} \33[34m é \33[33m {moeda108.moeda(moeda108.aumentar(num, 10))}')
print(f'\33[34mO desconto de 10% de \33[33m R${num:.0f} \33[34m é \33[33m {moeda108.moeda(moeda108.diminuir(num, 10))}')
toolbox.fimLinha()