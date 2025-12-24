from cores import cores

print(cores["verde"] + "-=" * 50)
print(cores['azul'] + f"{" Super Progressão Aritmética v3.0":=^100}")
print(cores['verde'] + "-=" * 50 + cores["limpa"])

DEBUG = False

primeirotermo = int(input('\33[34mDigite o Primeiro termo:\33[33m '))
razao = int(input('\33[34mDigite a razão:\33[33m '))

print(cores['verde'] + "-=" * 50 + cores["limpa"])

counter = 0
progrecao = primeirotermo
continuar = 1

text01 = ''
text02 = ''

total = 0
while True:
    
    if counter == 0:
        print(f'\33[34mSua progressão aritimetica é:\33[33m ')

    while counter < 10:  
        counter += 1
        total += 1
        text01 += str(f' {progrecao} -> ' if counter < 10 else f' {progrecao} ')
        progrecao += razao

        if counter == 10:
            print(text01.center(100, '-'))
            print(cores['verde'] + "-=" * 50 + cores["limpa"])

        
    while continuar > 0:

        continuar = int(input('\33[34mquantos termos voçe quer mostrar a mais:\33[33m '))
        
        
        if continuar == 0:
            break
        else:
            counter = 10
        
        while counter < continuar + 10:
            
            text02 += f'{progrecao} -> ' if counter < continuar + 9 else f'{progrecao}'
            progrecao += razao
            counter += 1
            total += 1
        if counter == continuar + 10:
            print(text02.center(100, '-'))
            print(cores['verde'] + "-=" * 50 + cores["limpa"])
            text02 = ''
        
        if DEBUG is True:
            print(f'\n\33[m#counter: {counter} #continuar: {continuar} #continuar + 10: {continuar + 10}')
            

        
        
    else:
        print(f'\33[32mFinalizado com {total} termos mostrados!')
        break

print('\33[33m' + '\33[31m Fim \33[33m'.center(110, 'x'), '\33[m')
