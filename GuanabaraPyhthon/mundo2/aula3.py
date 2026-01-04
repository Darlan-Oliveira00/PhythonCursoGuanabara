# sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
# print('Sexo {} registado com sucesso'.format(sexo))


# from random import randint
# computador = randint(0,10)
# print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
# print('Será que você consegue adivinhar qual foi?')
# acertou = False
# palpites = 0 
# while not acertou:
#     jogador = int(input('Qual é o seu palpite? '))
#     palpites += 1 
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print('Mais... Tente mais uma vez.')
#         elif jogador > computador:
#             print('Menos... Tente mais uma vez.')
# print('Acertou com {} tentativas. Parabéns!!'.format(palpites))





# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))
# opcao = 0
# while opcao != 5:
#     print('''    [ 1 ] Somar
#     [ 2 ] Multiplicar
#     [ 3 ] Maior
#     [ 4 ] Novos Números
#     [ 5 ] Sair do programa''')
#     opcao = int(input('Qual a sua opção? '))
#     if opcao == 1: 
#         soma = n1 + n2
#         print('O resultado da soma é: {}'.format(soma))
#     elif opcao == 2: 
#         multi = n1 * n2
#         print('O resultado da Multiplicação é: {}'.format(multi))
#     elif opcao == 3:
#         if n1 > n2:
#             maior = n1
#         else:
#             maior = n2
#         print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
#     elif opcao == 4: 
#         print('Informe o valor novamente: ')
#         n1 = int(input('Primeiro valor: '))
#         n2 = int(input('Segundo valor: '))
#     elif opcao == 5:
#         print('Finalizando...')
#     else:
#         print('Opção Inválida. Tenete Novamente')
# print('-=' *10)
# print('Fim do Programa! Volte Sempre.')



from math import factorial
n = int(input('Digite um número para calcular seu factorial: '))
f = factorial(n)
print('O factorial de {} é {}'.format(n, f))



n = int(input('Digite um número para calcular seu factorial: '))
c = n
f = 1 
print('Calculando {}! = '.format(n), end='')
while c > 0: 
    print('{} '.format(c), end='' )
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c 
    c -= 1
print('{}'.format(f))



print('GERADOR DE PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')



print('GERADOR DE PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('PAUSA')
mais = int(input('Quantos termos você quer mostrar? '))