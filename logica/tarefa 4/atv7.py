re_valor = int(input('digite o numero'))

lista = []
soma = 0

for i in range (re_valor, 0 , -1):
    lista.append(i) 
    soma += i

media = soma / len(lista) 

print(media)