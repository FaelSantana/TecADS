#Verificação de numero positivo, negativos ou Zero
def type_num(num:float)->str:
    if num > 0:
        return 'Positivo'
    elif num == 0:
        return 'Zero'
    else: return 'Negativo'
 
num = float(input('Digite um Número: '))
print(f'O Número {num} é: {type_num(num)}')
