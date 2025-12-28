def fatorial(num=1):
    f = 1 
    for c in range(num, 0, -1):
        f *= c
    return f

n = 6
print(fatorial(n))
print(fatorial())