
nota_um = float(input("Digite Sua primeira nota: "))
nota_dois = float(input("Digite sua segunda nota: "))

media = (nota_um + nota_dois) / 2

if media < 5:
    print("\033[31mReprovado\033[m")
elif media >= 5 and media <= 6.9:
    print("\033[33mRecuperacao\033[m")
else:
    print("\033[32maprovado\033[m")