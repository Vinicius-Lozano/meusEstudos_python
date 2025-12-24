print("\33[1;32m" + "~" * 145)
print('\33[34m' + f"{' Unindo dicionários e listas ':=^145}")
print('\33[1;32m' + "~" * 145 + '\33[m')

pessoa = {
    'nome': None,
    'sexo': None, 
    'idade':None
}

grupo = []

while True:
    print('\33[34minsira os dados: ')
    pessoa['nome'] = str(input('\33[34mNome:\33[33m '))
    pessoa['sexo'] = str(input('\33[34mSexo[m/f]:\33[33m '))
    pessoa['idade']= int(input('\33[34midade:\33[33m '))
    grupo.append(pessoa.copy())
    stop = input('\33[31mDeseja parar?\33[33m ').strip().lower()[0]
    
    print('\33[1;33m' + "~" * 145 + '\33[m')
    if stop in 's':
        break

pessoas_cadastradas = len(grupo)
idade_media = sum(pessoa['idade'] for pessoa in grupo) / len(grupo)

mulheres = []
for p in grupo:
    if p['sexo'] == 'f':
        mulheres.append(p['nome']) 
        
idade_maior = []
for p in grupo:
    if p['idade'] > idade_media:
        idade_maior.append(p['nome'])


print('\33[33mPessoas cadastradas: ')
print(''.join(f'{k:<15}' for k in pessoa.keys()))
line = '-' * 35
print(line.center(2))
for p in grupo:
    for v in p.values():
        print(f'{v:<15}', end = '')
    print()
print(line.center(2))

print(f'\33[34mforam cadastradas \33[33m{pessoas_cadastradas} \33[34mpessoas')
print(f'\33[34mdas pessoas cadastradas a idade media foi \33[33m{idade_media}')
print(f'\33[34mpor idade, essas pessoas estão acima da media: \33[33m{', '.join(str(p) for p in idade_maior)}')
if len(mulheres) > 0:
    print(f'\33[34mdas pessoas cadastradas \33[33m{', '.join(str(p) for p in mulheres)} \33[34mSão mulheres')
else:
    print('\33[34mSem mulheres na lista')

print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(159, 'x'), '\33[0;m')