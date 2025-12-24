print("\33[1;32m" + "~" * 150)
print('\33[34m' + f"{' Boletim com listas compostas ':=^150}")
print('\33[1;32m' + "~" * 150 + '\33[m')

matriz = []
print('\33[34mDigite os alunos e suas notas:')
while True:
    
    nome = str(input('\33[34mnome =>\33[33m '))
    nota1 = int(input('\33[34mNota 1 =>\33[33m '))
    nota2 = int(input('\33[34mNota 2 =>\33[33m '))
    
    matriz.append([nome, [nota1, nota2]])
    
    stop = input('\33[34mdeseja parar(s)?\33[31m ').strip()[0]
    if stop in 'Ss':
        break
print('\33[1;32m' + "~" * 150 + '\33[33m')
print('id'.ljust(5), 'Nome'.ljust(10), 'Media'.rjust(10))
line = '-' * 28
print(line.center(2))
for a in range(len(matriz)):
    print(str(a).ljust(5), str(matriz[a][0]).ljust(10), str(sum(matriz[a][1]) / len(matriz[a][1])).rjust(10))
print(line.center(2))
print('\33[0;34mquais notas deseja ver? [id] \33[33m')
while True:
    
    try:
        id = int(input('\33[34mid ou (s) sair => '))
        print(f'\33[34mNotas do aluno \33[33m{matriz[id][0]}: {matriz[id][1]}')
    except:
        break

print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(164, 'x'), '\33[0;m')