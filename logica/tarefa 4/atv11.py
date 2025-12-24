
m = 0
m_1maiora = float('-inf')
m_2menora = float('inf')
mulhera_lista = []
f_1maiora = float('-inf')
f_2menora = float('inf')
menor_mulher = ''

for i in range(1,11):
    nome =  input(f'nome da {i} pessoa ')
    sexo =  input(f'sexo da {i} pessoa ')
    altura = float(input(f'altura da {i} pessoa '))

    if sexo == 'm':
        m += 1
        if altura > m_1maiora:
            m_1maiora = altura
        if altura < m_2menora:
            m_2menora = altura

    elif sexo == "f":

        mulhera_lista.append(altura)
        if altura > f_1maiora:
            f_1maiora = altura
        if altura < f_2menora:
            f_2menora = altura
            menor_mulher = nome
    else:
        print('invalido')

media_mulher = sum(mulhera_lista) / len(mulhera_lista)

print(f"menor altura dos homens: {m_2menora} maior: {m_1maiora} de {m} homens")
print(f"menor altura das mulheres:{f_2menora} maior:{f_1maiora} em uma media de {media_mulher} sendo a menor mulher:{menor_mulher}")
