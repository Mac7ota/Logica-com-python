d = int(input("Por quantos dias ele ficou alugado ? "))
k = int(input("Qual a quilometragem marcada ? "))
v1 = d*60
v2 = k*0.15
print ("Pelos dados fornecidos o valor a se pagar e de aproxidamente {:.2f}".format(v1+v2))