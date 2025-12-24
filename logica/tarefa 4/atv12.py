
peso_lista = []
maior_idade = 0

for i in range(1,4):

    idade =  int(input(f'idade da {i} pessoa '))
    peso =  int(input(f'peso da {i} pessoa '))
    
    if idade >= 12:
        peso_lista.append(peso)
        if idade > maior_idade:
            maior_idade = idade

peso_media = sum(peso_lista) / len(peso_lista) 

print(f'A media de peso é: {peso_media} com a maior idade sendo {maior_idade}')


        
        



