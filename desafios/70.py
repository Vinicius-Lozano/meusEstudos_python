print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Estatísticas em produtos ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

counter = 0

sum_total = 0

counter_hprice = 0 

product_min_price = 0
product_min_price_name = ''

while True:
    
    input_name = input('\33[34mNome do Produto: \33[33m')
    input_price = float(input('\33[34mPreço do produto:\33[33m R$ '))
    counter +=1
    
    sum_total += input_price
    
    if input_price > 1000:
        counter_hprice += 1
    
    if counter == 1:
        product_min_price_name = input_name
        product_min_price = input_price
    else:
        if input_price < product_min_price:
            product_min_price = input_price
            product_min_price_name = input_name
    
    while True:
        stopper = input('\33[34mDeseja parar? (s/n):\33[33m ').upper().strip()[0]
        if stopper in 'SN':
            break
        
    print('\33[32m' + "~" * 150 + '\33[m')
            
    if stopper in 'S':
        break

print(f'\33[34mO total da sua compra é de : \33[33mR${sum_total}')
print(f'\33[34mA quantidade de produtos com mais de \33[32mR$1000\33[34m: \33[33m{counter_hprice}')
print(f'\33[34mO produto mais barato é \33[33m{product_min_price_name} \33[34mcustando \33[33mR$ {product_min_price}')

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')