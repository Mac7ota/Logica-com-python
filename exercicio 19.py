import random
a1 = str(input("Aluno um: "))
a2 = str(input("Aluno dois: "))
a3 = str(input("Aluno tres: "))
a4 = str(input("Aluno quatro: "))
l = [a1,a2,a3,a4]
e = random.choice(l)
print ("O aluno sorteado foi {}".format(e))