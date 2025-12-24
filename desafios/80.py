

list_num = []

for i in range(0,5):
    list_num.append(int(input('Digite um numero: ')))


list_num.insert(0, list_num.pop(list_num.index(min(list_num))))


last_num = list_num[0]

print(list_num)


    
for n in list_num:
    
    if n >= last_num:
        list_num.append(n)
        last_num = n
            

print(list_num)

        
        
    
        
            
