#Cálculo do IMC
def IMC(peso:int,altura:float)->float:
    return peso / (altura * altura)

print('Vamos Calcular o seu IMC')
peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura em Metros: '))
print(f'O seu IMC(índice de massa corpórea) é: {IMC(peso,altura):.2f}')
