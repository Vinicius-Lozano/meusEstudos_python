radar = int(input("Radar: "))

multa = (radar - 80) * 7

if radar <= 80:
    print("safe")
else:
    print("Vc foi multado em {} reais".format(multa))