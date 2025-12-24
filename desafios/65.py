print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Maior e Menor valores ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

DEBUG = False


numeros= []
counter = 0

while True:
    
    num = int(input('\33[34mDigite o valor:\33[33m '))
    numeros.append(num)
    counter += 1
    
    continuar = input('\33[34mDeseja continuar? [S/N]:\33[33m ').upper()
    if continuar == 'N':
        numeros.sort()
        media = sum(numeros) / len(numeros) 
        break



if DEBUG is True:
    print(numeros)
    print(f'maior: {numeros[-1]}')
    print(f'menor: {numeros[0]}')
    print(media)
    
print('\33[32m'+'\33[33m Os seus valores \33[32m'.center(160, '~'))
print(f'\33[34mQuantidade de numeros: \33[33m{counter}\n\33[34mMaior: \33[33m{numeros[-1]}\n\33[34mMenor: \33[33m{numeros[0]}\n\33[34mMedia: \33[33m{media}')

print('\33[33m' + '\33[31m Fim \33[33m'.center(160, 'x'), '\33[m')