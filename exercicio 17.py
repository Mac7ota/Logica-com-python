from math import hypot
#import math
c = float(input("Comprimento do cateto oposto: "))
d = float(input("Comprimento do cateto adjecente: "))
e = hypot(c,d)
#e = math.hypot(c,d)
#e = ((c**2+d**2)**(1/2))
print ("A hipotenusa vai medir {:.2f}".format(e))