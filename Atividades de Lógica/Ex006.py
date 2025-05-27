#Cálculo de Juros Simples
def juros_simples(vp:float,taxa:int,anos:float) -> float:
    return vp + (vp * taxa * anos / 100)

print('Vamos Calcular o Montante á taxa de Juros Simples')
vp = float(input('Digite o valor principal da aplicação: '))
taxa = int(input('Digite a taxa de juros: '))
anos = float(input('Digite o tempo em anos: '))
print(f'O Montante será {juros_simples(vp,taxa,anos)} R$')
