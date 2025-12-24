from cores import cores

sex = ""

print(cores["verde"] + "-=" * 50)
print(f"{" Homofobia ":=^100}")
print("-=" * 50 + cores["limpa"])

print(cores["verde"] + 'digite seu sexo [M/F]:')

while True:
    
    sex = str(input(cores['azul'] + "=> ").upper().strip())
    if sex in ["M", "F"]:
        break
    print(cores['vermelho'] + f"Esse sexo não existe {sex}")

print(cores['amarelo'])

if sex == "M":
    print('Seja Bem Vindo')
else:
    print('Seja Bem Vinda')

#print(cores['verde'] + f"Seja Bem Vindo(a) pessoa do sexo {sex}") 