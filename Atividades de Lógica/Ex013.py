#Verificação de número divisível por 3 e 5
num = int(input('Digite um número: '))
print(f'O Número {num} é divisível por 3 e 5' if num%3 == 0 and num%5 == 0 else f'O Número {num} não é divisível por 3 e 5')
