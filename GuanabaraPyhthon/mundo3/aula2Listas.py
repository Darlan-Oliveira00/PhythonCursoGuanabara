# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort()
# num.sort(reverse=True)
# num.insert(2, 2)
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não achei o número 4')
# print(num)
# print(f'Essa lista tem {len(num)} elementos')



# valores = []
# for cont in range (0,5):
#     valores.append(int(input('Digite um valor: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}')
# print('Cheguei ao final da lista')



# a = [2, 3, 4, 7]
# b = a[:]
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')



# listanum = []
# maior = 0
# menor = 0 
# for c in range (0, 5):
#     listanum.append(int(input(f'Digite um valor na posicão {c}: ')))
#     if c == 0:
#         maior = menor = listanum[c]
#     else:
#         if listanum[c] > maior:
#             maior = listanum[c]
#         if listanum[c] < menor:
#             menor = listanum[c]
# print('-='*30)
# print(f'Você digitou os valores {listanum}')
# print(f'O maior valor digitado foi: {maior} nas posições', end='')
# for i, v in enumerate(listanum):
#     if v == maior:
#         print(f'{i}... ', end='')
# print()
# print(f'O menor valor digitado foi: {menor} nas posições', end='')
# for i, v in enumerate(listanum):
#     if v == menor:
#         print(f'{i}...', end='')



# numeros = list()
# while True:
#     n = int(input('Digite um valor: '))
#     if n not in numeros:
#         numeros.append(n)
#         print('Valor adicionado com sucesso...')
#     else: 
#         print('Valor duplicado! Nåo vou adicionar...')
#     res = str(input('Quer continuar? [S/N] '))
#     if res in 'Nn':
#         break
# print('-='*30)
# print(f'Você digitou os valores {numeros}')



# lista = []
# for c in range (0, 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#     else:
#         pos = 0 
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos, n)
#                 break
#             pos += 1
# print('-='*30)
# print(f'Os valores digitados em ordem foram {lista}')




# valores = []
# while True:
#     valores.append(int(input('Digite um valor: ')))
#     res = str(input('Quer continaur? [S/N] '))
#     if res in 'Nn':
#         break
# print('-='*30)
# print(f'Você digitou {len(valores)} elementos')
# valores.sort(reverse=True)
# print(f'Os valores em ordem decrescente são {valores}')
# if 5 in valores:
#     print('O valor 5 faz parte da lista.')
# else:
#     print('O valor 5 não foi encontrado na lista')




# num = list()
# pares = list()
# impares = list()
# while True:
#     num.append(int(input('Digite um número: ')))
#     resposta = str(input("Quer continar? [S/N] "))
#     if resposta in 'Nn':
#         break
# for i, v in enumerate(num):
#     if v % 2 == 0:
#         pares.append(v)
#     else:
#         impares.append(v)
# print(f'A lista completa é {num}')
# print(f'Os ímpares são {impares}')
# print(f'Os pares são {pares}')


expr = str(input('Digite a expressão: '))
pilha = list()