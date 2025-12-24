from cores import cores

print(cores["verde"] + "-=" * 50)
print(cores['azul'] + f"{" Progreçao aritimetica ":=^100}")
print(cores['verde'] + "-=" * 50 + cores["limpa"])


primeirotermo = int(input('\33[34mDigite o Primeiro termo:\33[33m '))
razao = int(input('\33[34mDigite a razão:\33[33m '))
size = primeirotermo + (10-1) * razao

res = '\33[33m'

for i in range(primeirotermo, size + razao, razao):
    res += f'{i} -> '

res += 'Fim'

print(f'\33[34mSua progressão aritimetica é: {res}')
print('\33[33m' + '\33[31m Fim \33[33m'.center(110, 'x'), '\33[m')