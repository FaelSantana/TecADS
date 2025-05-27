#Classificação de idade
while True:
    idade = int(input('Digite uma idade: '))
    if idade < 12:
        print('Você é uma Criança')
    elif idade < 18:
        print('Você é um adolescente')
    elif idade < 30:
        print('Você é um Jovem adulto')
    else:
        print('Você é um Adulto')