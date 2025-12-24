from cores import cores

print(cores["verde"] + "-=" * 50)
print(cores['azul'] + f"{" Sequência de Fibonacci v1.0":=^100}")
print(cores['verde'] + "-=" * 50 + cores["limpa"])

sequecia = int(input('\33[34mQuantos termos deseja mostrar:\33[33m '))
counter = 0

num01 = 0
num02 = 1
num03 = 0
numeros = [0, 1]
while counter < sequecia:
    
    counter += 1 
    
    num03 = num01 + num02
    numeros.append(num03)
    num01 = num03 + num02
    numeros.append(num01)
    num02 = num01 + num03
    numeros.append(num02)


sqlimpa = ' -> '.join(str(num) for num in numeros[:sequecia])

print('\33[32m' + '~' * 100)
print(f'\33[34mOs termos que voçe decidiu mostar são:\n\33[33m{sqlimpa}')
print('\33[32m' + '~' * 100)


print('\33[33m' + '\33[31m Fim \33[33m'.center(110, 'x'), '\33[m')
  