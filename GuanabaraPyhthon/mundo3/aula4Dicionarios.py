# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(F'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.items())
# print(pessoas.values())
# print(pessoas.keys())
# del pessoas['sexo']
# pessoas['pesso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil)
# print(brasil[1]['sigla'])


# from random import randint
# from time import sleep
# from _operator import itemgetter
# jogo = {'jogador 1':randint(1,6),
#         'jogador 2':randint(1,6),
#         'jogador 3':randint(1,6),
#         'jogador 4':randint(1,6)} 
# print('Valores sorteados: ')
# ranking = list()
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado')
#     sleep(1)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# for i, v in enumerate(ranking):
#     print(f'{i+1} lugar: {v[0]} com {v[1]}')
#     sleep(1)


# from datetime import datetime
# dados = dict()
# dados['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de Nascimento: '))
# dados['idade'] = datetime.now().year -  nasc
# dados['ctps'] = int(input('Carteira de Trabalho: (0 não tem): '))
# if dados['ctps']!= 0:
#     dados['contração'] = int(input('Ano de Contratação: '))
#     dados['Salario'] = float(input('Salário: R$'))
#     dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
# print('-='*30)
# print(dados)