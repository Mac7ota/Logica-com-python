numero = float(input("Digite o valor a ser conferido : "))
valor = numero % 2
if valor == 0:
    print ("O numero {:.0f} e par".format(numero))
else:
    print ("O numero {:.0f} e impar".format(numero))

