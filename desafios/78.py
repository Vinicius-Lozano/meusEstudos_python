print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Maior e Menor valores na Lista ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')


num_list = []

for i in range(0, 5):
    num_list.append(int(input(f'\33[34mDigite um Numero para posiçao \33[31m{i}\33[34m:\33[33m ')))
print('\33[32m' + "~" * 150 + '\33[m')

max_num = max(num_list)
max_pos_list = []

min_num = min(num_list)
min_pos_list = []

for pos, num in enumerate(num_list):
    
    if num == max_num:
        max_pos_list.append(pos)
    elif num == min_num:
        min_pos_list.append(pos)
    
print(f'\33[34mlista de números \33[33m{num_list}')
print(f'\33[34mO maior número foi \33[31m{max_num} \33[34mna posiçao \33[33m{' | '.join(str(n) for n in max_pos_list)}')
print(f'\33[34mO menor número foi \33[31m{min_num} \33[34mna posiçao \33[33m{' | '.join(str(n) for n in min_pos_list)}')

print('\n\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')