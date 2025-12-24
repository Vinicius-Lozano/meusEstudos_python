print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Contando vogais em Tupla ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

words = ('python', 'caralho', 'aprender', 'macaco', 'aranha', 'golfinho', 'lapis', 'caderno')

for word in words:
    print(f'\n\33[34mNa palavra \33[33m{word} \33[34mtemos: \33[33m', end = ' ')
    for i in word:
        if i in 'aeiou':
            print(i, end=' ')

print()
print('\n\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')
