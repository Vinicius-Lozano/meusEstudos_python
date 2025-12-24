pessoas = {'nome': 'Joao', 'idade': 22, 'sexo': 'M'}

print(pessoas)
# {'nome': 'Joao', 'idade': 22, 'sexo': 'M'}
print(pessoas['nome'])
# Joao
print(f'o {pessoas['nome']} tem {pessoas["idade"]} anos')
# o Joao tem 22 anos

print(pessoas.keys())
# dict_keys(['nome', 'idade', 'sexo'])
print(pessoas.values())
# dict_values(['Joao', 22, 'M'])
print(pessoas.items())
# dict_items([('nome', 'Joao'), ('idade', 22), ('sexo', 'M')])

for k in pessoas.keys():
    print(k)
    
for v in pessoas.values():
    print(v)
    
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
pessoas['nome'] = 'Maria'
pessoas['peso'] = 90

print(pessoas)

brasil = []

estado1 = {'uf': 'Rio', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[1]['sigla'])

brasil.clear()

estado = dict()

for e in range(0, 3):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

for u in brasil:
    for k, v in u.items():
        print(f'o Campo {k} tem valor {v}')
        
for u in brasil:
    print(f'o estado {u["uf"]} tem a sigla {u["sigla"]}')