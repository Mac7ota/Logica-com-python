n1 = float(input("Valor do seu salario atual: "))

if n1 >= 1.250:
    n2 = (10*n1)/100+n1
    print("Seu salario recebeu um aumento de 10% passando a ser {}$".format(n2))
else:
    n3 = (15*n1)/100+n1
    print("Seu salario recebeu um aumento de 15% passando a ser {}$".format(n3))


