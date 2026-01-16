from math import trunc

num = float(input("Digite um número: "))
print("O valor digitado é {} e a sua porção inteira é {}".format(num, trunc(num)))
import math
catetoposto = int(input("Digite o valor do cateto oposto: "))
catetoadjacente = int(input("Digite o valor do cateto adjancente: "))
#hipotenusa = (catetoposto*2 + catetoadjacente*2) / (1/2)
hipotenusa = math.hypot(catetoadjacente, catetoposto)
print("A hipotenusa vale {}".format(hipotenusa))

frase = 'Curso em Vídeo Python'
# print(frase.upper().count('O'))
print(frase.find('Curso'))