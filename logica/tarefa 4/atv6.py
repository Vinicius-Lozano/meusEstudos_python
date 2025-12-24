

lista = []

while True:

    sim_nao = input('para continuar digite um numero para a media digite: m. ')

    if sim_nao == "m":
        break

    else:
        n1 = int(sim_nao)
        lista.append(n1)

s_i = sum(lista)
m_i = s_i / len(lista)
print(m_i)




