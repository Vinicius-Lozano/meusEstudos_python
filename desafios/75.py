print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Análise de dados em uma Tupla ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

t = ()
tp = ()

for i in range (0, 4):
    input_user = int(input('\33[34mDigite numeros 4 vezes:\33[33m '))
    ti = (input_user,)
    t += ti
    if input_user % 2 == 0:
        tp += ti

try:
    t3 = f'\33[34mO numero 3 Foi digitado na Posição: \33[33m{t.index(3) + 1}'
except:
    t3 = '\33[34mO numero 3 não foi digitado'
    
print(f'\33[34mA sua lista é: \33[34m{t}')
print(f'\33[34mA quantidade de vezes que apareçe o numero 9: \33[33m{t.count(9)}' )
print(t3)
print(f'\33[34mOs numeros pares são:\33[33m' , ', '.join(str(n) for n in tp))

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')