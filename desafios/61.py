from cores import cores

print(cores["verde"] + "-=" * 50)
print(cores['azul'] + f"{" Progreçao aritimetica com while ":=^100}")
print(cores['verde'] + "-=" * 50 + cores["limpa"])


primeirotermo = int(input('\33[34mDigite o Primeiro termo:\33[33m '))
razao = int(input('\33[34mDigite a razão:\33[33m '))

print(cores['verde'] + "-=" * 50 + cores["limpa"])

counter = 0
progrecao = primeirotermo

while True:
    
    if counter == 0:
        print(f'\33[34mSua progressão aritimetica é:\33[33m ', end='')
        
    if counter < 10:  
        counter += 1
        print(progrecao, end=' -> ')
        progrecao += razao 
        
    else:
        print('fim')
        break

print('\33[33m' + '\33[31m Fim \33[33m'.center(110, 'x'), '\33[m')
