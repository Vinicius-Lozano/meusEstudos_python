from datetime import datetime

cores = {"limpa":"\033[m", "verde": "\033[32m", "azul": "\033[34m", "vermelho": "\033[31m"}

print(cores["verde"] + "-=-=-" * 8)
print("{:=^40}".format("Alistamento militar"))
print("-=-=-" * 8 + cores["limpa"])

ano_nas = int(input(cores["azul"] + "Digite o ano em que voce nasceu: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nas

if idade < 18:
    falta = 18 - idade
    print(f'voce ainda e novo para se alistar, vc tem{cores["verde"]} {idade} {cores["azul"]}anos ainda faltam{cores["vermelho"]} {falta} {cores["azul"]}anos para o seu alistamento')
elif idade > 18:
    sobra = idade - 18
    print(f"voce passou do ano de se alistar, vc tem {cores['verde']}{idade}{cores['azul']} anos se passaram {cores['vermelho']}{sobra}{cores['azul']} anos do seu alistamento")
else:
    print(f"{cores['verde']}voce esta no ano de se alistar!{cores['limpa']}")