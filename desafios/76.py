print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Lista de Preços com Tupla ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

slist = ('Lapis', 1.50, 'Caneta', 2, 'Caderno', 18.25, 'Granpeador', 3, 'Regua', 2.20, 'Borracha', 1.50, 'Massinha', 20, 'Estojo', 6.50, 'Livro', 62.75)

print()

print('\33[33m' + '-' * 84)
print('\33[34mLista de Preços'.center(84))
print('\33[33m' + '-' * 84)

for i in range(0, len(slist), 2):
    print(f'\33[34m{slist[i]:.<75}R${slist[i + 1]:>7.2f}')

sum_ = sum(slist[i] for i in range(1, len(slist), 2))

print('\33[33m' + '-' * 84)
print(f'{'Total: R$':>72}{sum_:>7.2f}')
print('\33[33m' + '-' * 84)

print('\n\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')

