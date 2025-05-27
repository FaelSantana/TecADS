#Cálculo de área de um retângulo

def calc_area(lar:float,com:float)->float:
    return lar * com

lar = float(input('Digite a largura de retângulo: '))
com = float(input('Digite o Comprimento de um retângulo: '))
print(f'A área do retângulo é {calc_area(lar,com)} M²')
