# n = s = 0
# while True < 3:
#     n = int(input("Digite um número: "))
#     if n == 999:
#         break
#     s += n 
# print('A soma vale {}'.format(s))


soma = cont = 0
while True:
    num = int(input('Digite um valor [999 para parar] '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores é: {soma}!')