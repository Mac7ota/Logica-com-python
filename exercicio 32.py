from datetime import date
ano = int(input("Ano a ser lido: Coloque 0 se quiser que o ano atual seja analisado: "))
if ano ==0:
    ano= date.today().year

if ano%4==0 and ano%100!=0 or ano %400==0:
    print("O ano {} e bissexto".format(ano))
else:
    print("O ano {} não e bissexto".format(ano))