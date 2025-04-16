def style_print(dic:dict)-> None:
    print('-'*len(dic['Nome']))
    print(dic['Nome'].upper())
    print('-'*len(dic['Nome']))

    for key in list(dic.keys()):
        print(f'{key.title()}: {dic[key].title()}')    
    pass
Pessoas = []

while True:
    print('-'*23)
    print('Vamos Cadastrar Pessoas')
    print('-'*23)
    Pessoas.append({
        'Nome':input('Digite o Nome: '),
        'Idade':int(input('Digite sua idade: ')),
        'Sexo':input('Digite seu sexo: '),
        'rua': input('Digite sua rua: '),
        'Bairro': input('Digite Seu Bairro: '),
        'Cidade': input('Digite sua Cidade: ')
    })
    if input('Deseja Continuar? [s/n]: ') in 'Nn':
        break
c = 0
for pessoa in Pessoas:
    print(f'\t[{c}]:{pessoa[list(pessoa.keys())[0]]}')
    c += 1
    pass

while True:
    style_print(Pessoas[int(input('Revelar Dados: '))])
    if input('Deseja Continuar? [S/N]: ') in 'Nn':
        break