t = str(input('Qual falor a ser lido para identificar o seu tipo : '))

print ('Qual o tipo primitivo de leitura ?{} '.format(type(t)))
print ('So tem espaçoes ?{} ',t.isspace())
print ('E um numero ?{} ',t.isnumeric())
print ('E alfabetico ?{} ',t.isalpha())
print ('E afalnumerico ?{} ',t.isalnum())
print ('E maiuscula ?{} ',t.isupper())
print ('E minuscula ?{} ',t.islower())
print ('Esta capitalizada ?{} ',t.istitle())