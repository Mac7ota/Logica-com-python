import random
import time
computador = random.randint(0,5)
print ("-=-" *20)
print ("Vou pensar em um numero de 0 a 5 tente advinhar.....")
print ("-=-" *20)

jogador = int(input("Em que numero eu pensei? "))
print ("Processando aguarde....")
time.sleep(3)

if jogador == computador:
    print ("Parabens voce acertou o numero que eu pensei")
else:
    print ("Poxa voce errou, eu pensei no {} e não no {}" .format(computador,jogador))