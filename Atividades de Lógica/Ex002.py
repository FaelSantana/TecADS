#Conversor de temperaturas
'''
Faça um programa que converta uma temperatura em Celsiu para Fahrenheit
'''
def temp_converter(Celsius:float)->float:
    Fahr = (Celsius * 9/5) + 32
    return Fahr

print('Conversor de Temperaturas')
Celsius = float(input('Digite uma Temperatura em Celsius: '))
print(f'A temperatura em {Celsius} Cº em Fahrenheit é {temp_converter(Celsius)}º')
