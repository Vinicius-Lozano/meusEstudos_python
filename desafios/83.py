print("\33[1;32m" + "~" * 150)
print('\33[34m' + f"{' Validando expressões matemáticas ':=^150}")
print('\33[1;32m' + "~" * 150 + '\33[m')

eq = input('\33[34mDigite uma expressão para checar se falta algum paretese => \33[33m').replace(' ','')

eq_list = list(eq)

back_count = eq_list.count('(')
front_count = eq_list.count(')')

print('\33[1;32m' + "~" * 150 + '\33[m')
if back_count == front_count:
    print('\33[1;32mA sua expressão esta sem erros!')
else:
    print(f'\33[1;31mNa sua expressão falta fechar \33[33m{abs(back_count - front_count)} \33[31mparenteses!')

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')