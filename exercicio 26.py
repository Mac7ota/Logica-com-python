f = str(input("Qual a frase : ")).upper() .strip()
k = f.count('A')
j = f.find('A')
m = f.rfind('A')

print ("Quantidade de letras A: {}\nQuando se inicia: {}\nQuando acaba: {}".format(k,j,m))