print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Tuplas com Times de Futebol ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

times = ('cruzeiro', 'flamengo', 'palmeiras', 'red bull', 'bota fogo', 'bahia', 'mirassol', 'fluminense', 'atletico',
         'internacional', 'corinthias', 'sao paulo', 'ceara', 'gremio', 'vitoria', 'vasco', 'santos', 'juventude', 'fortaleza', 'sport')

print(f'\33[34mLista de times \33[33m{times}')

print('\33[32m' + "~" * 150 + '\33[m')

print(f'\33[34mOs cinco primeiros colocados são \33[33m{times [0:5]}')
print(f'\33[34mOs ultimos quatro colocados \33[33m{times[-4:]}')
print(f'\33[34mEm Ordem alfabetica: \33[33m{sorted(times)}')

print(f'\33[34mE o time Mirassol esta na \33[33m{times.index("mirassol") + 1}ª \33[34mposiçao')

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')