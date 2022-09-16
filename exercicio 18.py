import math
a = float(input("Angulo a ser calculado: "))
b = math.sin(math.radians(a))
c = math.cos(math.radians(a))
d = math.tan(math.radians(a))
print ("Valor cogitado em\nSeno {} \nCosseno {} \nTangente {} ".format(b,c,d))