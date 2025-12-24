num = int(input("Escolha um numero para converter nas bases numericas: "))

base = int(input("""
=====Bases=====                                 
Binario     (1)
Octal       (2)
Hexadecimal (3)
===============                  
escolha a base numerica: """))

if base == 1:
    print("A conversao é de: {}".format(bin(num)[2:]))
elif base == 2:
    print("A conversao é de: {}".format(oct(num)[2:]))
elif base == 3:
    print("A conversao é de: {}".format(hex(num)[2:]))
else:
    print("Opcao n Existe")