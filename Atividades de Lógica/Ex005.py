#Cálculo de Desconto
def desconto(valor:float,desc:int)->float:
    valor_final = valor - (valor * desc/100)
    return valor_final

print('Vamos Calcular o valor final de um produto aplicado o desconto')
valor = float(input('Digite o valor do produto: '))
desc = int(input('Digite a taxa de desconto: '))
print(f'O valor final do produto é {desconto(valor,desc):.2f} R$')
