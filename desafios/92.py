from datetime import date

print("\33[1;32m" + "~" * 145)
print('\33[34m' + f"{' Cadastro de Trabalhador em Python ':=^145}")
print('\33[1;32m' + "~" * 145 + '\33[m')

nome =  str(input('\33[34mNome:\33[33m '))
ano_nas = int(input('\33[34mAno de nascimento:\33[33m '))
ctps = int(input('\33[34mCarteira de trabalho (0):\33[33m '))
idade = date.today().year - ano_nas

if ctps > 0:
    ano_contr = int(input('\33[34mDigite o ano de contratação:\33[33m '))
    salario = int(input('\33[34mDigite o seu salario:\33[33m R$'))
    contrib = idade + (35 - (date.today().year - ano_contr))
else:
    ano_contr = 'Não Consta'
    salario = 'Não Consta'
    contrib = 'Não Consta'

pessoa = {'Nome': nome, 
          'Ano NAS': ano_nas, 
          'idade': idade,
          'CTPS': ctps, 
          'Ano Con': ano_contr,
          'Aposento': contrib,
          'Salário': salario}

print('\33[1;32m' + "~" * 145 + '\33[m')
info_array = [f'\33[34m{k}: \33[33m{v}' for k,v in pessoa.items()]
print(f' | '.join(info_array))
print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(159, 'x'), '\33[0;m')