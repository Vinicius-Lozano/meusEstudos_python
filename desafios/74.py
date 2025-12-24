from random import randint

print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Maior e menor valores em Tupla ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

while True:
    t = ()
    for i in range(0, 5):
        tuple_ = (randint(1, 10),)
        t += tuple_
        
    print(f'\33[34msua tupla gerada: \33[33m{t}')
        
    print(f'\33[34mMenor numero da tupla: \33[33m{min(t)}, \33[34mMaior numero da tupla: \33[33m{max(t)}')
    
    stopper = input('\33[34mParar?\33[33m ').upper()[0]
    del(t)
    
    if stopper in 'S':
        print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')
        break