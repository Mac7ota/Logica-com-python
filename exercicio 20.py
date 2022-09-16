import random
a1 = str(input("Primeiro aluno "))
a2 = str(input("Segundo aluno "))
a3 = str(input("Terceiro aluno "))
a4 = str(input("Quarto aluno "))
e = [a1,a2,a3,a4]
l = random.sample(e,4)

print ("A sequencia sorteada ficou como {}".format(l))
