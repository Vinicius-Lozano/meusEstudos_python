from cores import cores
from random import randint

debug = False

print(cores["verde"] + "-=" * 50)
print(cores['azul'] + f"{" Jogo de Adivinhar ":=^100}")
print(cores['verde'] + "-=" * 50 + cores["limpa"])


num_bot = randint(0, 10)
num_player = 99

counter = 0

print(cores['azul'] + 'Pensei em um numero de 0 a 10!')

while num_player != num_bot:
    
    num_player = int(input(cores['vermelho'] + 'Advinhe o numero: ' + cores['amarelo']))
    counter += 1
    
    if num_player > num_bot:
        print('Esse numero é maior do que eu pensei')   
    elif num_player < num_bot:
        print('E numero é menor do q eu pensei')
    
    if debug is True:
        print(f'num bot: {num_bot} num player: {num_player} counter: {counter}')

print(cores['verde'] + f'Voçe acertou! depois de \33[33m {counter} \33[32m tentativas, O numero era \33[33m{num_bot}')

