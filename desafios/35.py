
lado_um = int(input("digite o Primeiro lado do Triangulo: "))
lado_dois = int(input("Digite o Segundo lado do triangulo: "))
lado_tres = int(input("Digite o terceiiro lado do triangulo: "))

lados = [lado_um, lado_dois, lado_tres]
lados.sort()

print(lados[0],lados[1],lados[2])

if lados[2] < lados[0] + lados[1]:
    print("pode formar um triangulo")
else:
    print("nao forma um triangulo")
    
print("menor:", lados[0])
print("maior:", lados[2])