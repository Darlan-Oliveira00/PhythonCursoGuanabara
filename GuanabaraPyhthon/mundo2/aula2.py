# inicio = int(input('inicio: '))
# fim = int(input('fim: '))
# passo = int(input('passo: ')) 
# for c in range (inicio, fim+1, passo):
#     print(c)
# print('FIMMM')

# s = 0
# for c in range (0, 3):
#     n = int(input('Digite um número: '))
#     s += n
# print('O somatorio de todos os valores foi {}'.format(s))
# print(f"a soma foi de {s}")
# print('FIM')


# import time
# for c in range (1,11):
#     print(c)
#     time.sleep(1)
# print('BUMM BUMM')


# for c in range (1, 51, 2):
#     # if c % 2 ==0:
#     #     print(c)
#     print(c, end=' ')
# print('ACABOUUU')


# s = 0
# for c in range (1, 501, 2):
#     if c % 3 == 0:
#         s += c
# print('A soma total é: {}'.format(s))


# num = int(input('Digite um número para ver sua tabauda: '))
# for c in range (1,11): 
#     r = num * c
#     print(f'{num} x {c} = {r}')
#     print('-='*5)
#     print(f"{num} x {c} = {num*c} ")


# soma = 0
# for c in range (1, 7):
#     num = int(input('Digite o {} número: '.format(c)))
#     if num % 2 == 0:
#         soma = soma + num
#     else:
#         print('O número {} é IMPAR será desconsiderado'.format(num))
# print("A soma total dos números PARES é: {}".format(soma))



print("="*10)
print('10 TERMOS DE UMA PA')
print("="*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro, decimo + razao, razao):
    print("{}".format(c), end=" -> ")
print('ACABOU')