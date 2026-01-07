lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# # for cont in range (0, len(lanche)):
# #     print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# for pos, c in enumerate(lanche):
#      print(f'Eu vou comer {c} na posição {pos}')
# print('Comi pra caramba')



# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(sorted(lanche))
# print(lanche)



# a = (2, 5, 4)
# b = (8, 5, 1, 2)
# c = a + b
# print(c)
# print(c.index(8))


# pessoas = ('Darlan', 19, 'M',55.60)
# del(pessoas)
# print(pessoas)



cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze',
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Você digitou o número {cont[num]}')