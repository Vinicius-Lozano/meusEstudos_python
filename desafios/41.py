from datetime import datetime

ano_nas = int(input("Digite o ano em que voce nasceu: "))
idade = datetime.now().year - ano_nas

if idade <= 9:
    categoria = "mirim"
elif idade <= 14:
    categoria = "infantil"
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 20:
    categoria = "Senior"
else:
    categoria = "Master"

print(f"Voce tem \033[33m{idade}\033[m anos e se encaixa na categoria \033[32m{categoria}\033[m")