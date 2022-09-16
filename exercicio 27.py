n = str(input("Qual o seu nome completo : ")).strip()
k = n.split()
print ("O primeiro nome e {} ".format(k[0]))
print ("O ultimo nome e {}".format(k[len(k)-1]))
