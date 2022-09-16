n = str(input("Qual o seu nome completo ? "))
l = n.upper()
m = n.lower()
print ("O seu nome todo maiusculo e {} \nO seu nome todo minusculo e {}".format(l,m))

p= n.replace(' ','')
o = len(p)
print ("A quantidade de caracteres do seu nome {} sem contar espaços".format(o))

j = n.split()
print ('A quantidade de letras do seu primeiro nome e {}'.format(len(j[0])))
