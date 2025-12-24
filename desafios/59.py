from cores import cores

print(cores["verde"] + "-=" * 50)
print(cores['azul'] + f"{" Mais ou menos uma Calculadora ":=^100}")
print(cores['verde'] + "-=" * 50 + cores["limpa"])

num01 = int(input( cores['azul'] + 'Digite o Primeiro numero: ' + cores['amarelo']))
num02 = int(input( cores['azul'] + 'Digite o segundo numero: ' + cores['amarelo']))

print(cores["verde"] + "-=" * 50)

command = ['', 'Somar', 'Multiplicar', 'Maior dos numeros', 'Novos numeros', 'Fechar']

while True:
    
    print (f'{cores['azul']}Escolha a operaçao que deseja fazer\n\33[32m[{cores['amarelo']}1{cores['verde']}] somar\n[{cores['amarelo']}2{cores['verde']}] Multiplicar\n[{cores['amarelo']}3{cores['verde']}] Maior dos numeros\n[{cores['amarelo']}4{cores['verde']}] Novos numeros\n[{cores['amarelo']}5{cores['verde']}] Sair')
    operacao = int(input('\33[34mDigite a operação:\33[33m ')) 
    
    if operacao not in (1, 2, 3, 4, 5 ):
        print(cores['vermelho'] + '\33[33m Operaçao invalida tente novamente! \33[31m'.center(110, 'x'))
        continue
    
    print(cores['verde'] + '-=' * 50)
    print(f'\33[31mPrimeiro numero: \33[33m{num01}\33[32m | \33[31mSegundo numero: \33[33m{num02} \33[32m| \33[31mOperação: \33[33m{command[operacao]}'.center(140), '\n')
    
    if operacao == 4:

        num01 = int(input('\33[34mDigite o novo primeiro numero:\33[33m '))
        num02 = int(input('\33[34mDigite o novo segundo numero:\33[33m '))  
        print(cores["verde"] + "-=" * 50)
        continue
        
    if operacao != 5:
        
        if operacao == 1:
            
            resultado = num01 + num02
            query = "Soma dos numeros"
            
        elif operacao == 2:
            
            resultado = num01 * num02
            query = "multiplicaçao dos numeros"
        
        elif operacao == 3:
            
            numSort = [num01, num02]
            numSort.sort()
            resultado = numSort[-1]
            query = "Maior dos numeros"
            
            if num01 == num02:
                print('\33[34mOs numeros são iguais')
                print(cores['verde'] + '-=' * 50)
                continue
    
        print(f'\33[34mO resultado de {query} é: \33[33m{resultado}')
        print(cores['verde'] + '-=' * 50)
        
    else:
        print('\n\33[31m' + f'\33[33m {command[operacao]} \33[31m'.center(110, 'x'))

        break