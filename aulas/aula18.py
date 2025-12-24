pessoas = []
grupo = []

pessoas.append('joao')
pessoas.append('18')

print(pessoas)

grupo.append(pessoas[:]) #AQUI é basicamente fatie toda a lista pessoas e coloque na outra ai serve como se fosse uma copia

pessoas[0] ='maria'
pessoas[1] ='29'

print(pessoas)

grupo.append(pessoas[:]) 
# em vez de linkar uma na outra vai simplesmente copiar a existente 
# a = 1 2 3 | b = a | b[0] = 99 => a = 99 2 3
# a = 1 2 3 | b = a[:] | b[0] = 99 => a = 1 2 3 | b = 99 2 3

print(grupo)

grupo.append(['jose', '30'])
grupo.append(['pedro', '34'])
print(grupo)
print(grupo[0][0])
print(grupo[0][1])