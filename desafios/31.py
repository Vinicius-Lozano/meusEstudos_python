travelDis =  int(input("Distancia da viagem: "))

if travelDis <= 200:
    print('O preco da viagem e de {} reais'.format(travelDis*0.5))
else:
    print('O preco da viagem e de {} reais'.format(travelDis*0.45))