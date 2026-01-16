n = int (input("Digite um numero: "))
a = n - 1
s = n + 1

d = n * 2
t = n * 3
raiz = n ** (1/2) #REPRESENTAÇÃO DA RAIZ QUADRADA

print("Analisando o sucessor de {} é {} e o antecessor é {} ".format(n, s, a))
print("O dobro de {} é {} ".format(n, d))
print("O triplo de {} é {}".format(n, t))
print("A raiz de {} é {:.2f}".format(n, raiz))
print("A raiz de {} é {:.2f}".format(n, pow(n, (1/2))))


nota1 = float(input ("Digite a primeira nota: "))
nota2 = float(input ("Digite a segunda nota: "))

r = (nota1 + nota2) / 2

print("Sua média é: {}".format(r))

num = int (input("Digite um numero para ver a tabuada: "))
print("{} x {:2} : {}".format(num, 1, num*1))
print("{} x {:2} : {}".format(num, 2, num*2))
print("{} x {:2} : {}".format(num, 3, num*3))
print("{} x {:2} : {}".format(num, 4, num*4))
print("{} x {:2} : {}".format(num, 5, num*5))
print("{} x {:2} : {}".format(num, 6, num*6))
print("{} x {:2} : {}".format(num, 7, num*7))
print("{} x {:2} : {}".format(num, 8, num*8))
print("{} x {:2} : {}".format(num, 9, num*9))
print("{} x {:2} : {}".format(num, 10, num*10))
print("Obrigado por contribuir cada vez mais...")