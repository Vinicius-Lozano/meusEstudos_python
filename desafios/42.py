lado_um = int(input("digite o Primeiro lado do Triangulo: "))
lado_dois = int(input("Digite o Segundo lado do triangulo: "))
lado_tres = int(input("Digite o terceiiro lado do triangulo: "))

lados = [lado_um, lado_dois, lado_tres]
lados.sort()

print(lados[0],lados[1],lados[2])

if lados[2] < lados[0] + lados[1]:
    print("pode formar um triangulo")

    if lados[0] == lados[1] and lados[0] == lados[2]:
        print('triangulo equilatero')
    elif lado_um == lado_dois or lado_um == lado_tres or lado_dois == lado_tres:
        print('Triangulo isoseles')
    else:
        print('escaleno')

else:
    print("nao forma um triangulo")


    
print("menor:", lados[0])
print("maior:", lados[2])