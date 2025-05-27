#Cálculo com desconto com condição

def calc_cond(valor:float,desc:int)->None:
    print(valor - (valor * desc/100) if valor > 100 else 'Impossivel calcular desconto para valores menores que 100')
    pass

while True:
    valor = float(input('Digite o valor do produto: '))
    desc = int(input('Digite o valor de desconto: '))
    calc_cond(valor,desc)
    pass