import toolbox

toolbox.cabecalho(' Ficha do Jogador ')

def ficha(nome, gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = 0
        
    jogador = {'nome': nome, 'gol': gol}
    return f'\33[34mO jogador \33[33m{jogador["nome"]} \33[34mfez \33[33m{jogador["gol"]} \33[34mGols'

nome = input('\33[34mNome:\33[33m ')
gols = input('\33[34mGols:\33[33m ')
print(ficha(nome, gols))