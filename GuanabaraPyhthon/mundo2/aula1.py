nome = str(input('Qual é seu nome?? '))
if nome == 'Gustavo':
    print("Que nome bonito!")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Seu nome é bem popular no Brasil")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Que nome bonito feminino")
else: 
    print("Seu nome é bem normal.")
print("Tenha um Bom Dia, {}!".format(nome))



casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual valor do seu salário? R$"))
anos = int(input("Quantos anos você vai pagar? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa, anos), end="")
print(" a prestação será de R${:.2f}".format(prestacao))
if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO")
else: 
    print("Empréstimo NEGADO")



num = int(input("Digite um numero interio: "))
print('''Escolha uma das bases para converão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num) [2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num) [2:]))
else:
    print('Opção Inválida!! TENTE NOVAMENTE.')





from datetime import date
atual = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE")
elif idade < 18:
    saldo = 18 - idade 
    print("Ainda faltam {} anos para o alistamento".format(saldo))
    ano =  atual + saldo
    print("Seu alistamento será em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))




nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print("Tirando {:.1} e {:.1}, a média do aluno é {:.1}".format(nota1, nota2, media))
if media >= 5 and media < 7:  
    print("O aluno está em RECUPERAÇÃO.")
elif media < 5:
    print("O aluno está REPROVADO.")
else: 
    print("O aluno está APROVADO.")




from datetime import date
atual = date.today().year
nascimento = int(input("Ano de Nascimento: "))
idade = atual - nascimento
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print('Classificacão: MIRIM')
elif idade <=  14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmentos: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else: 
        print('ISÓCELES!')


peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print ('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25: 
    print('Parabens você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO') 
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
else: 
    print('Você está em OBESIDADE MÓRBIDA, cuidado!') 