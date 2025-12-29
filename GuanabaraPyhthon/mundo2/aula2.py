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



# print("="*10)
# print('10 TERMOS DE UMA PA')
# print("="*10)
# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# decimo = primeiro + (10 - 1) * razao
# for c in range (primeiro, decimo + razao, razao):
#     print("{}".format(c), end=" -> ")
# print('ACABOU')



# num = int(input('Digite um número: '))
# total = 0
# for c in range (1, num + 1):
#     if num % c == 0:
#         print('\033[33m', end=' ')
#         total += 1
#     else:
#         print('\033[31m', end=' ')
#     print(f"{c}", end=' ')
# print('\n\033[mO número {} foi divisível {} vez'.format(num, total))
# if total == 2:
#     print('E por isso é PRIMO!')
# else:
#     print('E por isso ele NÃO É PRIMO')


# frase =str(input('Digite uma farse: ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range (len(junto) - 1, -1, -1):
#     inverso += junto[letra]
# if inverso == junto:
#     print('Temos um palíndormo!!')
# else:
#     print('A farse digitada não é um palíndromo')


# from datetime import date
# atual = date.today().year
# totmaior = 0
# totmenor = 0 
# for pess in range (1, 8):
#     nasc = int(input('Em que a pessoa nasceu? '))
#     idade = atual - nasc
#     if idade >= 21:
#         totmaior += 1
#     else:
#         totmenor += 1
# print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
# print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))



# maior = 0
# menor = 0 
# for p in range (1, 6):
#     peso = float(input('Peso da {} pessoa: '.format(p)))
#     if p == 1:
#         maior = p
#         menor = p
#     else: 
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print('O maior peso lido foi {}'.format(maior))
# print('O menor peso lido foi {}'.format(menor))


somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for c in range (1, 6):
    print('-------- {} PESSOA --------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20: 
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média das idade do grupo é de {} anos'.format(mediaidade))
print('O homen mais velho tem {} anos e se chama {}'.format(maioridadehomen, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))