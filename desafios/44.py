cores = {
    "limpa": "\033[m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m"
}

print(cores["verde"] + "-=" * 50)
print(f"{"Compra e Forma de pagamento":=^100}")
print("-=" * 50 + cores["limpa"])

preco = float(input(cores["azul"] + 'Digite o Valor do produto: ' + cores["amarelo"]))
f = int(input(cores["azul"] + "Forma de pagamento? Dinheiro/cheque(0), cartao a vista(1), cartao 2x(2), cartao 3x(3): " + cores["amarelo"]))

print(cores["verde"] + "--" * 50)

if f == 0:
    valor = preco - preco *0.1
    print(cores["azul"] + "Sera pago o valor a vista, Se aplica o disconto de 10%")
    print(f"O Preco do seu produto era \033[32mRS${preco:.2f}\033[34m o valor com desconto: \033[32mRS${valor:.2f}\033[m")

elif f == 1:
    valor = preco - preco * 0.05
    print(cores["azul"] + "Sera pago no cartao a vista, se aplica disconto de 5%")
    print(f"O Preco do seu produto era \033[32mRS${preco:.2f} RS\033[34m o valor com desconto: \033[32mRS${valor:.2f}\033[m")

elif f == 2:
    valor = preco
    print(cores["azul"] + 'Sera pago no cartao de 2x o valor do protudo sera normal')
    print(f"total a pagar \033[32m{valor:.2f}")

elif f == 3:
    valor = preco * 1.20
    print(cores["azul"] + "Sera pago no cartao de 3x, o valor do produto sera 20% mais caro")
    print(f"O preco do seu produto era \033[32mRS${preco}\033[34m, aogora o total a pagar: \033[32mRS${valor}")

else:
    print("Forma de pagamento inexistente")

