print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Número por Extenso ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

numbers = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('\33[34mDigite um numero de 0 a 20:\33[33m '))

while num not in range(0, 21):
    num = int(input('\33[34mNumero não reconhecido digite no entervalo de 0 a 20:\33[33m '))

print(f'\33[34mVoçe digitou o numero \33[33m{num}\33[34m / \33[33m{numbers[num]} ')

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')
    