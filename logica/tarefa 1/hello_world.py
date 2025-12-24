import math

#Atv01
nota_01 = int(input('escreva a sua primeira nota: '))
nota_02 = int(input('escreva a sua segunda nota: '))
print('sua media é de {}'.format((nota_01+nota_02)/2))
#atv02

r=float(input('escreva o raio: '))
a= (r**2) * 3.14159
print(f'a area é de: {a:.4f}')

#atv03
print('Vou converter metros para centimetros e mm')

n5 = int(input('quantos metros: '))

ncm = n5*100
nmm = n5*1000

print('{}M, {}Cm, {}mm'.format(n5, ncm, nmm))

#atv04
nota_03 = int(input('escreva a sua terceira nota: '))
media_p = ((nota_01 * 2) + (nota_02 * 3) + (nota_03 * 5)) /3
print('sua média é de: {:.1f}'.format(media_p))

#atv05

print('avo \n     Pai \n          neto')

#atv06

print('Silvio\nSantos\nSilva' )

#atv07
nota_04 = int(input('Primeiro numero: '))
nota_05 = int(input('elevado: '))
elevado = math.pow(nota_04,nota_05)
print(elevado)

#atv08
x=10
y=49
z=25
e = (2 * x)-(y * 0.07) + (z * 5)
print('o resultado é:', e)

#atv09

nome_01 = input('primeiro nome: ')
nome_02 = input('segundo nome: ')
nome_03 = input('terceiro nome: ')

print('nomes entrada:', nome_01, nome_02, 'e', nome_03)
print('nomes saida:',nome_03, nome_02, 'e', nome_01 )

#atv10

tempo_horas = int(input('tempo em horas '))
velocidade_media = int(input("velocidade media "))

litros_gastos = (velocidade_media * tempo_horas) / 12
print('litros gastos: {:.3f}'.format(litros_gastos))
