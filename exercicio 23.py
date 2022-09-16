v = int(input("O valor a ser diagnosticado : "))
u = str(v)
r = v//1%10
t = v//10%10
d = v//100%10
m = v//1000%10
print ("Analisando o numero {}".format(v))
print ("Unidade {} ".format(r))
print ("Dezena {} ".format(t))
print ("Centena {} ".format(d))
print ("Milhar {} ".format(m))

