from random import randint
from time import sleep

print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Jogo do Par ou Ímpar ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

counter = 0

while True:
    
    bot_choice_finger = randint(1, 10)
    player_choice_side = input('\33[34mImpa, Par?\33[33m ').upper().strip()[0]
    
    player_choice_text = 'Par' if player_choice_side == 'P' else 'Impar'
    
    if player_choice_side not in ['P', 'I']:
        print('\33[34mO Bot não conseguiu te entender, voçe quer \33[31mIMPAR OU PAR?\33[33m ')
        continue
    
    player_choice_finger = int(input('\33[34mJogue seus dedos:\33[33m '))
    
    game_sum = bot_choice_finger + player_choice_finger
    
    print('\33[32m' + "~" * 150 + '\33[33m')
    
    text_counting = '123i..'
    
    for t in text_counting:
        print(t, end=' ', flush= True)
        sleep(0.5)
        
    print(' JÁ!')
    sleep(0.6)
        
    print(f'\33[34mSeus dedos: \33[33m{player_choice_finger} \33[34mdedos do bot: \33[33m{bot_choice_finger} \33[34mentão deu... \33[33m{game_sum}!')
    sleep(3.5)
    
    if game_sum % 2 == 0:
        res = ['P', 'Par']
    else:
        res = ['I', 'Impar']
        
    print(f'\33[34mDeu \33[33m{res[1]} \33[34me voçe escolheu \33[33m{player_choice_text} \33[34mentão...')
    sleep(3)
    
    if player_choice_side in res[0]:
        
        print('\33[1;32mganhou!\33[m')
        print('\33[32m' + "~" * 150 + '\33[m')
        print('\33[31mBot: \33[1;34mQuero revanche!\33[m')
        
        counter += 1
    else:
        print('\33[1;31mPerdeu!\33[m')    
        print('\33[32m' + "~" * 150 + '\33[m')
        break

print(f'\33[34mO jogo acabou e voçe acabou conseguindo vencer \33[33m{counter}\33[34m', 'vez!' if counter == 1 else 'vezes!')
print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')