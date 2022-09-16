viagem = float(input("Quantos KM sera a sua viagem? "))
cidade = str(input("Qual a cidade de destino? "))
if viagem <=200:
    print("O valor a ser pago na sua viagem e {:.2f} reais".format(viagem*0.50))
else:
    print("O valor a ser pago na sua viagem e {:.2f} reais".format(viagem*0.45))
print("-=-"*20)
print("Tenha uma boa viagem para {}".format(cidade))
print("-=-"*20)