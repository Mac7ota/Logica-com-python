import time
v = int(input("Qual a velocidade que seu veiculo estava : "))
print ("Processando valor fornecido aguarde.........")
time.sleep(5)
if v > 80:
    print ("A velocidade maxima de circulação e de 80km/h e por isso seu veiculo foi multado ")
    multa = (v-80) * 7
    print ("Cada km/h excedido tem uma taxa de 7,00 reais, total do valor a pagar {:.2f}".format(multa))
else:
    print ("Seu veiculo circulou na velocidade de {}km/h respeitando a velocidade permitida no local".format(v))
