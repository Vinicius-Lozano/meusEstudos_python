lanche = ('hamburger', 'suco', 'pizza', 'pudim', 'batata')
print(lanche)

print('-'*50)

for cont in range(0, len(lanche)):
    print(f'lanches {lanche[cont]}')

print('-'*50)

for pos, comida in enumerate(lanche):
    print(f'lanches {comida} position {pos}')