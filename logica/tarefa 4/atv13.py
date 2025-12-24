
idade_50 = 0
altura_lista = []
peso_40 = 0


for i in range(1,13):
    idade =  int(input(f'idade da {i} pessoa '))
    peso =  int(input(f'peso da {i} pessoa '))
    altura = float(input(f'altura da {i} pessoa '))

    if idade > 50:
        idade_50 += 1
    if idade in range (10,21):
        altura_lista.append(idade)
    if peso < 40:
        peso_40 += 1

if len(altura_lista) > 0:
    altura_media = sum(altura_lista) / len(altura_lista)
    print(f'media de altura entre 10 e 20 anos:{altura_media}')

porcentagem = (peso_40 / 12) * 100

print(f'pessoas com mais de 50 anos:{idade_50} porcentagem inferior a 40kg: {porcentagem}')
