lista = [1, 4, 5, 6, 7]
print(f'Lista = {lista}')

lista[3] = 2 
print(f'Lista[3] = 2 : {lista}')

lista.append(2)
print(f'lista.append(8) {lista}')

lista.sort(reverse= True)
print(f'lista.sort(reverse= True) {lista}')

lista.insert(2, 0)
print(f'lista.insert(2, 0) {lista}')

lista.pop(2)
print(f'lista.pop(2) {lista}')

lista.remove(2)
print(f'lista.remove(2) {lista}')

if 5 in lista:
    lista.remove(5)
print(lista)

for pos, num in enumerate(lista):
    print(f'on {pos} exists {num} - ')

for cont in range(0, 5):
    lista.append(int(input('Digite Valores: ')))
print(lista)