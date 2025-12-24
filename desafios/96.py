import toolbox

toolbox.cabecalho(' Função que calcula área ')

def area(comp, larg):
    area = comp * larg
    print(f'\33[34mA área desse terreno de \33[33m{comp} \33[34mde comprimento e \33[33m{larg} \33[34mde largura é de \33[33m{area}m²')


comprimento = int(input('\33[34mComprimento do terreno:\33[33m '))
largura = int(input('\33[34mLargura do terreno:\33[33m '))

toolbox.linha()

area(comprimento, largura)

toolbox.fimLinha()
