estacoes = ['outono','inverno','primavera','verão']
#Exibindo a tupla
print(f'As quatro estações do ano: {" ".join(estacoes)}')

#Acessando elementos da tupla pelo índice
c = 0
for estacao in estacoes:
    c += 1
    print(f'{c}ª estacão: {estacao}')
    pass

#tamanho da tupla
print(f'Quantidade de estações do ano {len(estacoes)}')

#Percorrendo a tupla com um loop
print([estacao for estacao in estacoes])

#Verificando se um elemento está na tupla
print('outono está na lista' if 'outono' in estacoes else 'outono não está na lista')

#Criando um tupla de um único elemento
tupla_unica = ('melão')
print(f'tupla de um único elemento {tupla_unica}')
