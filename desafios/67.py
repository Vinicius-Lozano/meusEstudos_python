print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Tabuada v3.0 ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

num = 0

while True:
    
    num = int(input('\33[34mDigite o Valor da Tabuada que deseja:\33[33m '))
    
    if num < 0:
        break
    
    print('\33[32m' + ' \33[1;34mTABUADA\33[0;32m '.center(164, '~'))
    
    for i in range(1, 6):
        print(f'\33[34m{num}  X {i:>2} = \33[33m{num * i:>3} | \33[34m{num}  X {i + 5:>2} = \33[33m{num * (i + 5):>3}')
    print('\33[32m' + "~" * 150 + '\33[m')

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')