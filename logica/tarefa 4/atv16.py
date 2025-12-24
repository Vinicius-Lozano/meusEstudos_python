
q_c = 0
q_s = 0
soma_idades = 0
q_v = 0
q_d = 0
total_pessoas = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    e_c = input("Digite o estado civil: ")
    outra = input("quer adicionar outra pessoa?(s/n): ")
    
    if e_c == 'c':
        q_c += 1
    elif e_c == 's':
        q_s += 1
    elif e_c == 'v':
        q_v += 1
        soma_idades += idade
    elif e_c == 'd':
        q_d += 1

    if outra == "n":
        break
    
    


    total_pessoas += 1

if q_v > 0:
    media_v = soma_idades / q_v
else:
    media_v = 0

if total_pessoas > 0:
    porce_d = (q_d / total_pessoas) * 100
else:
    porce_d = 0

print(f"pessosas casadas:{q_c} pessoas solteiras:{q_s} viuvas: {q_v} porcentagem de divorciados{porce_d}")


