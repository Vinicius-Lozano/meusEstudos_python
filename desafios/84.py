print("\33[1;32m" + "~" * 150)
print('\33[34m' + f"{' Lista composta e analise de dados ':=^150}")
print('\33[1;32m' + "~" * 150 + '\33[m')

pessoa = list()
grupo = list()

pessoas_p = list()
pessoas_L = list()

maior_p = 0
menor_p = 0
maior_p_nome = ''
menor_p_nome = ''

print('\33[34mDigite o nome e o peso para adicionar a lista')
while True:

    nome = str(input('\33[34mnome =>\33[33m '))
    peso = int(input('\33[34mpeso =>\33[33m '))
    pessoa.append(nome)
    pessoa.append(peso)
    grupo.append(pessoa[:])
    
    pessoa.clear()
    
    stop = input('\33[31mParar?\33[33m ').strip()[0]
    if stop in 'SsPpAa':
        break

total = len(grupo)
maior_p = grupo[0][1]
menor_p = grupo[0][1]
maior_p_nome = grupo[0][0]
menor_p_nome = grupo[0][0]

for p in grupo:
     
    if p[1] > maior_p:
        
        maior_p = p[1]
        maior_p_nome = p[0]
    elif p[1] < menor_p:
        
        menor_p = p[1]
        menor_p_nome = p[0]          
       
    if p[1] > 90:
        pessoas_p.append(p[0])
    elif p[1] <= 75:
        pessoas_L.append(p[0])

print('\33[1;32m' + "~" * 150 + '\33[m')
print(f'\33[34mNo total Foram cadastradas \33[33m{total} \33[34mpessoas')
print(f'onde a pessoa mais pesada foi \33[33m{maior_p_nome} \33[34mcom \33[33m{maior_p}Kg')
print(f'\33[34mcom essas pessoas ultrapassando 90kg \33[33m{' | '.join(str(pp) for pp in pessoas_p)}')
print(f'\33[34mA pessoa mais leve foi \33[33m{menor_p_nome}\33[34mcom \33[33m{menor_p}kg')
print(f'\33[34me as pessoas com menos de 75kg são \33[33m{' | '.join(str(pl) for pl in pessoas_L)}')
print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')