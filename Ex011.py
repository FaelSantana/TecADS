#Classificação de triângulos
def triangulo(lados:list)->str:
    for x in lados:
        #teste Eqjuilátero
        if lados[0] == lados[1] and lados[0] == lados[2]:
            return 'Equilátero'
        
        #teste Isósceles
        for x in lados:
            lados.pop(lados.index(x))
            if x == lados[0] and x != lados[1]:
                return 'Isósceles'
            pass
        
        #teste Escaleno
        if lados[0] != lados[1] and lados[0] != lados[2]:
            return ('Escaleno')
        

lados = [int(input('Digite um Comprimento: ')) for x in range(3)]
print(f'O triângulo é {triangulo(lados)}')
