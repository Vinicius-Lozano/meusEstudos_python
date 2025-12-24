total_v = 0
total_l = 0
total_a = 0
total_h = 0

while True:
    codigo = input("Digite o código: ")
    
    if codigo == 'f':
        break

    valor = float(input("Digite o valor: "))
    total_v += valor

    if codigo == 'l':
        total_l += valor
    elif codigo == 'a':
        total_a += valor
    elif codigo == 'h':
        total_h += valor

print(f"total geral {total_v}, toral L:{total_l}, total A:{total_a}, total H:{total_h}")