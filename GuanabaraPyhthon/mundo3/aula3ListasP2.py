# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)



# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

# galera = list()
# dado = list()
# totmaior = totmenor = 0 
# for c in range (0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade')
#         totmaior += 1
#     else:
#         print(f'{p[0]} é menor de idade')
#         totmenor += 1
# print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade.')



# temp = []
# princ = []
# maior = menor = 0 
# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Peso: ')))
#     if len(princ) == 0:
#         maior = menor = temp[1]
#     else:
#         if temp[1] > maior:
#             maior = temp[1]
#         if temp[1] < menor:
#             menor = temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     resposta = str(input('QUER CONTINUAR? [S/N] '))
#     if resposta in 'Nn':
#         break
# print('-='*30)
# print(princ)
# print(f'Ao todo você cadrastrou {len(princ)} pessoas.')
# print(f'O maior pesso é {maior}. Peso de ', end='')
# for p in princ:
#     if p[1] == maior:
#         print(f'{p[0]} ', end='')
# print()
# print(f'O menor pesso é {menor}', end='')
# for p in princ:
#     if p[1] == menor:
#         print(f'{p[0]}', end='')
# print()



num = [[], []]
valor = 0 