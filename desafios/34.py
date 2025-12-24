sal = float(input("digite o salario: "))

if sal > 1250.00:
    a = 10 
    al = sal * 1.10 - sal
else:
    a = 15
    al = sal * 1.15 - sal

print('o seu aumento foi de {} totalizando um acressimo de {:2g} Reais'.format(a, al))




