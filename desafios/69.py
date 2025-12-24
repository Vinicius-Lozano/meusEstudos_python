print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Análise de dados do grupo ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

counter_age = 0
counter_man = 0
counter_woman = 0

while True:
    
    value_sex = input('\33[34mDigite o sexo:\33[33m ').upper().strip()[0]
    
    if value_sex not in 'MF':
        continue
    
    value_age = int(input('\33[34mDigite a idade:\33[33m '))
    
    if value_age >= 18:
        counter_age += 1
    
    if value_sex in 'M':
        counter_man += 1
    elif value_sex in 'F' and value_age < 20:
        counter_woman += 1

    while True:
        stopper = input('\33[34mDeseja Continuar?\33[33m ').strip()[0]
        if stopper in 'NnSs':
            break
        
    print('\33[32m' + "~" * 150 + '\33[m')     
    if stopper in 'nN':
        break
    
print(f'\33[34mPessoas com mais de 18: \33[33m{counter_age}')
print(f'\33[34mHomens cadastrados: \33[33m{counter_man}')
print(f'\33[34mMulheres com menos de 20 anos: \33[33m{counter_woman}')

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')