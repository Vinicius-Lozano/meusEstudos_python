print("\33[1;32m" + "~" * 145)
print('\33[34m' + f"{' Dicionário em Python ':=^145}")
print('\33[1;32m' + "~" * 145 + '\33[m')

nome = str(input('\33[34mDigite o nome do aluno:\33[33m '))
media = float(input('\33[34mDigite a media do aluno:\33[33m '))
situacao = None

aluno = {'nome': nome, 'media': media, 'situacao': None}

if media < 7:
    situacao = 'REPROVADO'
else:
    situacao = 'APROVADO'

aluno['situacao'] = situacao

print(f'\33[34mNome: \33[33m{aluno["nome"]} \33[34m| Média: \33[33m{aluno["media"]} \33[34m| Situação: \33[33m{aluno["situacao"]}')

print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(159, 'x'), '\33[0;m')