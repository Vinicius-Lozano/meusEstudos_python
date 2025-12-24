def somatorio_entre_numeros(num1, num2):
    # Garantir que num1 seja menor ou igual a num2
    if num1 > num2:
        num1, num2 = num2, num1
    
    # Usando a função sum e range para calcular o somatório
    somatorio = sum(range(num1, num2 + 1))
    
    return somatorio

# Recebendo os dois números do usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Calculando e mostrando o somatório
resultado = somatorio_entre_numeros(numero1, numero2)
print(f"O somatório dos números entre {numero1} e {numero2} é {resultado}.")



def soma_primeiros_impares(n):
    soma = 0
    contador_impares = 0
    numero = 1

    while contador_impares < n:
        if numero % 2 != 0:  # Verifica se o número é ímpar
            soma += numero
            contador_impares += 1
        numero += 1

    return soma

# Calculando a soma dos 200 primeiros ímpares
soma = soma_primeiros_impares(200)

print("A soma dos 200 primeiros números ímpares é:", soma)