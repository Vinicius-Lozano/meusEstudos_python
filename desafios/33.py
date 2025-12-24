num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
num3 = int(input('digite o terceiro numero: '))
nM=0

if nM < num1:
    nM = num1
    mm = nM

if nM < num2:
    nM = num2
    mm = num1

if nM < num3:
    nM = num3

if mm > num2:
    mm = num2

if mm > num3:
    mm = num3


print(nM)
print(mm)