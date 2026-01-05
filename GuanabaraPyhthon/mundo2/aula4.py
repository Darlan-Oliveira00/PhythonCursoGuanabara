# n = s = 0
# while True < 3:
#     n = int(input("Digite um número: "))
#     if n == 999:
#         break
#     s += n 
# print('A soma vale {}'.format(s))


# soma = cont = 0
# while True:
#     num = int(input('Digite um valor [999 para parar] '))
#     if num == 999:
#         break
#     cont += 1
#     soma += num
# print(f'A soma dos {cont} valores é: {soma}!')


# while True: 
#     n = int(input('Quer ver a tabuada de qual valor? '))
#     if n < 0:
#        break 
#     print('-'*30)
#     for c in range (1, 11):
#         print(f"{n} x {c} = {n*c}")
#     print('-'*30)
# print('PROGRAMA TABUADA ENCERRADA. Volte Sempre!')



# from random import randint
# v = 0
# while True:
#     jogador = int(input('Diga um valor: '))
#     computador = randint(0,10)
#     total = jogador + computador
#     tipo = ' '
#     while tipo not in 'PI':
#         tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
#     print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end='')
#     print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR ')
#     if tipo == 'P':
#         if total % 2 == 0:
#             print('Você VENCEU!!')
#             v += 1
#         else: 
#             print('Você PERDEU!! ')
#             break
#     elif tipo == 'I':
#         if total % 2 == 1:
#             print('Você VENCEU!!')
#             v += 1
#         else: 
#             print('Você PERDEU!!')
#             break
#     print('Vamos joagr Novamente...')
#     print('-='*15)
# print(f'GAME OVER! Você venceu {v} vezes.  ')
# print('-='*15)



while True: 
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo sexo not in  'MF:'
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
