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



listanum = []
maior = 0
menor = 0 
for c in range (0, 5):
    listanum.append(int(input(f'Digite um valor na posicão {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('-='*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi: {maior} nas posições', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi: {menor} nas posições', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')