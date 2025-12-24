print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Tratando vários valores v1.0 ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')


num = 0
counter = 0
sum_ = 0

num = int(input('\33[34mDigite os Valores \33[31m[999 = STOP]:\33[33m '))

while num != 999:
    
    sum_ += num
    counter +=1
    num = int(input('\33[34mDigite os Valores \33[31m[999 = STOP]:\33[33m '))
    

print("\33[32m" + "~" * 150)
print(f'\33[34mForam digitados \33[33m{counter}\33[34m numeros e a soma deles deu \33[33m{sum_}')
print('\33[33m' + '\33[31m Fim \33[33m'.center(160, 'x'), '\33[m')
