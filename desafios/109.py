import moeda109
import toolbox

toolbox.cabecalho(' Exercitando módulos em Python ')

num = float(input('\33[34mDigite o preço desejado: \33[33mR$'))
print(f'\33[34mA metade de \33[33m R${num:.0f} \33[34m é \33[33m {moeda109.metade(num, False)}')
print(f'\33[34mO dobro de \33[33m R${num:.0f} \33[34m é \33[33m {moeda109.dobro(num, True)}')
print(f'\33[34mO aumento de 10% de \33[33m R${num:.0f} \33[34m é \33[33m {moeda109.aumentar(num, 10, True)}')
print(f'\33[34mO desconto de 10% de \33[33m R${num:.0f} \33[34m é \33[33m {moeda109.diminuir(num, 10, True)}')
toolbox.fimLinha()