import toolbox
import json
toolbox.cabecalho(' Mini Projeto Python ')



while True:
    toolbox.paragrafo(' Menu ', 'azul')
    print(' \33[33m1 \33[34m- \33[32mVer Pessoas cadastradas')
    print(' \33[33m2 \33[34m- \33[32mCadastrar Nova pessoa')
    print(' \33[33m3 \33[34m- \33[31mSair')
    toolbox.linha('~','azul')
    
    try:
        escolha = int(input('\33[32mEscolha:\33[33m '))
    except ValueError:
        toolbox.linha(char='~',cor='amarelo')
        print('\33[31m', 'Digite um Numero!'.center(60))
        toolbox.linha(char='~',cor='amarelo')
        continue
    
    if escolha == 1 or escolha == 2:
        try: 
            with open('desafios/115.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
 
        except FileNotFoundError:
            print('\33[31mNão existe Pessoas cadastradas')
            print('\33[33mCadastre o Primeiro!')
            
            nome = str(input('\33[32mNome:\33[33m '))
            idade = int(input('\33[32mIdade:\33[33m '))
            pessoa = {'pessoas': [{'nome': nome, 'idade': idade}]}
            with open('desafios/115.json', 'w', encoding='utf-8') as f:
                json.dump(pessoa, f, indent=4, ensure_ascii=False)
            continue
    
    if escolha == 1:
        
        print('\33[33m','Pessoas cadastradas'.center(60))
        toolbox.linha('-', 'amarelo')
        for pessoa in data['pessoas']:
            print(f'Nome: {pessoa['nome']}'.ljust(35), f'Idade: {pessoa['idade']}')
        toolbox.linha('-', 'amarelo')
            
    if escolha == 2:
        print('\33[34mCadastre a nova pessoa! ')
        
        nome = str(input('\33[32mNome:\33[33m '))
        idade = int(input('\33[32mIdade:\33[33m '))
        nova_pessoa = {'nome': nome, 'idade': idade}
        data['pessoas'].append(nova_pessoa)
        
        with open('desafios/115.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
    
    if escolha == 3:
        break
    
    if escolha > 3 or escolha < 1:
        print('\33[31mComando NÂO RECONHECIDO tente outro!')

toolbox.fimLinha()