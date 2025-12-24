from random import randint

NunRand = randint(0, 5)
# print(NunRand)

NunUser = int(input('digite um numero de 0 a 5: '))

if NunUser == NunRand:
    print('VC venceu!!')
else:
    print("vc Perdeu :(")   