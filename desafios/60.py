from cores import cores

print(cores["verde"] + "-=" * 50)
print(cores['azul'] + f"{" Leitor de fatorial ":=^100}")
print(cores['verde'] + "-=" * 50 + cores["limpa"])

num01 = int(input('\33[34mDigite um Numero para saber o seu fatorial:\33[33m '))
num00 = num01
fat = 1
calc = ''

while num01 >= 1:
    
    calc += f'{num01} X ' if num01 > 1 else f'{num01} = '
    fat = fat * num01 
    num01 -= 1
    
print(f'\33[34mO Calculo da fatorial é:\33[33m {num00}!= {calc}{fat}')
print(cores['verde'] + "-=" * 50 + cores["limpa"])