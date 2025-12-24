#Exercicios durante a aula
sddsVida = input("digite seu nome: ")
feijao = int(input("digite sua idade: "))
bola = float(input('digite sua altura: '))
print(f'Seu nome é {sddsVida} sua idade é {feijao} sua altura é {bola}')
print(type(sddsVida), type(feijao), type(bola))

numero = 3.1414141414
print("{:.2f}".format(numero))

#Atv01
numberOne= int(input("digite um número: "))
numberTwo= int(input("digite outro número: "))

totalNumbers = numberOne+numberTwo
print("A soma deles se equivale a: {}" .format(totalNumbers))

#Atv02
nomeSujeito = input("digite seu nome: ")
anoAtual = int(input("Digite o ano Atual: "))
anoNascimento = int(input("Digite seu ano de nascimento: "))
idadeSujeito = anoAtual-anoNascimento

print("Olá, {}. Você possui {}, anos" .format(nomeSujeito, idadeSujeito))

#Atv03
abacate = int (input("digite o seu saldo: "))
feijao = int (input("digite o valor da retirada: "))
pipa = abacate-feijao
print(f"restara apenas {pipa}")

#Atv04
ano_nas = int(input('Escreva o ano de nascimento '))
ano_atual= int(input("Digite o ano Atual: "))
mes_nasc = int(input('mes em numero '))
dias_nasc = int(input('dia em que nasceu '))
idade_dias = (ano_atual - ano_nas) * 365  + dias_nasc + (mes_nasc * 30)

print('você tem {} anos e aproximadamente {} dias'.format(ano_atual-ano_nas, idade_dias))

#Atv05
h = int(input("Digite a altura do triângulo: "))
l = int(input('digite a largura do triângulo: '))
a = h * l / 2

print(f"A area do triângulo é de {a}cm quadrados")

