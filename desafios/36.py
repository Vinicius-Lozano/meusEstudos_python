print("\033[1;32m=-=-=-" * 17)
print("'{:^100}'".format("Calculadora de emprestimo!"))
print("=-=-=-" * 17+"\033[m")

casa = float(input("digite o valor da casa: "))
salario = float(input('digite o seu salario: '))
pagarAnos = int(input("em Quantos anos deseja pagar: "))

print("\n"+"\033[92m=-=-\033[m" * 17,"\n")

if casa / (pagarAnos * 12) <= salario * 0.30:
    print("Emprestimo: \033[1;32mAceito\033[m")
    print('Sua parcela sera de \033[31m{:.2f}\033[m durante \033[31m{}\033[m meses'.format(casa/(pagarAnos*12), pagarAnos * 12))
else:
    print("Emprestimo: \033[1;31mNegado\033[m")