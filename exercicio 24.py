c = str(input("Qual o nome da cidade : ")).strip() .upper()
o = c.split()
d = ('SANTO' in o[0])
print ("A cidade possui Santo no inicio : {}".format(d))