i = int(input("informe i: "))
b = int(input("informe para b: "))

if i > b :
    print("INVALIDO i precisa ser menor que b")
else:
    sigma = sum(range(i,b+1))

print(f'O somatorio entre i: {i} e b:{b} é {sigma}')

