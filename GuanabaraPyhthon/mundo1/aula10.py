tempo = int(input("Quantos anos tem seu carro? "))
if tempo <= 3:
    print("Carro Novo")
else:
    print("Carro Velho ")
print("--- FIM ---")

nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print("Nome lindo você tem!")
print("Bom dia {}!".format(nome))


from random import randint 
computador = randint(0, 5)
print("-=-"*20)
print("VOU PENSAR EM UM NÚMERO ENTRE 0 E 5")
print("-=-"*20)
jogador = int(input("Em que número eu pensei? "))
if jogador == computador:
    print("PARABÉNS, Você consegui me vencer!!")
else:
    print("GANHEI!! Eu pensei no número {} não no número {}".format(computador, jogador))



num = int(input("Digite um numero qualquer: "))
if num%2 == 0:
    print("O número {} é par".format(num))
else: 
    print("O número {} é impar".format(num))


km = int(input("Qual a distância em KM: "))
if km <= 200:
    preco = km * 0.50
else: 
    preco = km * 0.45
print("O preço da sua passagem é: {}".format(preco))


from datetime import date
ano = int(input("Qual ano quer analisar? Coloque 0 para verificar o ano atual "))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100  != 0 or ano%400 == 0:
    print("O ano {} é BISSEXTO".format(ano))
else: 
    print("O ano {} NÃO É BISSEXTO".format(ano))


a = int(input("Primeiro valor: "))
b = int(input("Segundo valor:  "))
c = int(input("Terceiro valor: "))

if a<b and a<c: 
    menor = a
if b<c and b<a:
    menor = b; 
if c<b and c<a:
    menor = c
if a>b and a>c: 
    maior = a
if b>c and b>a:
    maior = b; 
if c>b and c>a:
    maior = c
print("O menor valor é {}".format(menor))
print("O maior valor é {}".format(maior))


salario = float(input("Qual o salário do funcionário? R$"))
if salario <= 1250:
    novo = salario + (salario * 15 / 100) 
else: 
    novo = salario + (salario * 10 / 100)
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora".format(salario, novo))



print("-="*20)
print("ANALISADOR DE TRIÂNGULOS")
print("-="*20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segemetos acima PODEM FORMAR triângulo")
else: 
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")



print('{:=^40}'.format(" LOJAS GUANABARA "))
preco = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qaul é a opção? ')) 
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco 
    parcela = total / 2
    print('Sua compra será parcelado em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelado em {:.2f}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente Novamente!')
print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(preco, total))


from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
print('KEM')
print('PÔ!!!')
print('')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else: 
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else: 
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else: 
        print('JOGADA INVÁLIDA')