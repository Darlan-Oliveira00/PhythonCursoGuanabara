n = s = 0
while True < 3:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n 
print('A soma vale {}'.format(s))


soma = cont = 0
while True:
    num = int(input('Digite um valor [999 para parar] '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores é: {soma}!')


while True: 
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
       break 
    print('-'*30)
    for c in range (1, 11):
        print(f"{n} x {c} = {n*c}")
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADA. Volte Sempre!')



from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            v += 1
        else: 
            print('Você PERDEU!! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            v += 1
        else: 
            print('Você PERDEU!!')
            break
    print('Vamos joagr Novamente...')
    print('-='*15)
print(f'GAME OVER! Você venceu {v} vezes.  ')
print('-='*15)



tot18 = tothomens = totM20 =  0
while True: 
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in  'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18: 
         tot18 += 1
    if sexo == 'M':
         tothomens += 1
    if sexo == 'F' and idade < 20:
         totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de Homens: {tothomens}')
print(f'Total de Mulheres com menos de 20 anos é {totM20}')




total = tot1000 = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        tot1000 += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco 
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1000,00 ')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')



print('-='*30)
print('{:^30}'.format('BANCO CEV'))
print('-='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor 
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else: 
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced ==10: 
            ced = 1
        totced = 0
        if total == 0: 
            break