try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except ZeroDivisionError:
    print('Não é possível dividir por Zero')
except Exception as error:
    print(f'O erro encontrado foi: {error.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre')