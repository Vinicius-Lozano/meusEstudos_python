n = 0
s = 0

while True:
    
    n = int(input('numero: '))
    
    if n == 999:
        break
    s += n
    
print(f'a soma vale{s}')