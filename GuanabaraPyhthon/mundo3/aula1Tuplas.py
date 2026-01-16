lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# for cont in range (0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, c in enumerate(lanche):
     print(f'Eu vou comer {c} na posição {pos}')
print('Comi pra caramba')



lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))
print(lanche)



a = (2, 5, 4)
b = (8, 5, 1, 2)
c = a + b
print(c)
print(c.index(8))


pessoas = ('Darlan', 19, 'M',55.60)
del(pessoas)
print(pessoas)



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



from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), 
     randint(1,10), randint(1,10),)
print('Os Valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')


num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'* 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'* 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('-'*40)




palavras = ('aprender', 'programar', 'linguagem', 'phython',
            'curso', 'gratis', 'estudar', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')