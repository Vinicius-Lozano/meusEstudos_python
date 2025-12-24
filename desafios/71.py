print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Simulador de Caixa Eletrônico ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

cel_count_50 = cel_count_20 = cel_count_10 = cel_count_01 = 0



while True:
    
    input_draw = int(input('\33[34mInforme o valor a ser sacado: \33[33mR$'))
    
    while True:   
              
        if input_draw == 0:
            break
        
        if input_draw >= 50:
            input_draw -= 50
            cel_count_50 += 1
        elif input_draw >= 20:
            input_draw -= 20
            cel_count_20 += 1
        elif input_draw >= 10:
            input_draw -= 10
            cel_count_10 += 1
        else:
            input_draw -= 1
            cel_count_01 += 1
        
            
    if input_draw == 0:
        break

cells = [
    {'cont': cel_count_50, 'name': '50'}, 
    {'cont': cel_count_20, 'name': '20'},
    {'cont': cel_count_10, 'name': '10'},
    {'cont': cel_count_01, 'name': '1'}
]

for cel in cells: 
    if cel['cont'] > 0:
        print(f'\33[34mRecebeu \33[33m{cel["cont"]}' , '\33[34mcédulas de' if cel['cont'] > 1 else '\33[34mcédula de' , f'\33[33mR${cel["name"]}')

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')
