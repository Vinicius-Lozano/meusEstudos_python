print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Vários números com flag ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')



count = 0
valores = 0

while True:
    
    valor = int(input('\33[34mDigite os Valores \33[31m[999 = STOP]:\33[33m '))
    
    if valor == 999:
        break
    
    count += 1
    valores += valor
    

print("\33[32m" + "~" * 150)
print(f'\33[34mForam digitados \33[33m{count}\33[34m numeros e a soma deles deu \33[33m{valores}')
print('\33[33m' + '\33[31m Fim \33[33m'.center(160, 'x'), '\33[m')
