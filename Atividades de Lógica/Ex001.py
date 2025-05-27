#Preço a pagar
'''
Criar um Porgrama que pede um valor de café ao usuário e a quantidade de cafés que ele irá comprar.
Retornar o valor total dos cafés
'''

def coffe_value(p:float,q:int)->int:
    price = q * p
    return price

p = float(input('Digite o Valor do café: '))
q = int(input('Digite a quantidade de cafés que irá comprar: '))
print(f'Você ira pagar {coffe_value(p,q)} R$')
